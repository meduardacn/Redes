# python3 simulador.py b.txt N1 N3 helloworld
# python3 simulador.py a.txt n1 n2 hello

import sys
from classes import Node
from classes import Router
from classes import Node_router
from classes import Routertable
from classes import ARP_Request_response
from classes import ARP_Reply_response
from classes import ICMP_Echo_Request_response
from classes import ICMP_Echo_Reply_response
def readFile():
    global topologyFile
    f = open(topologyFile, 'r')
    f = f.read() 
    f = f.split("#")
    nodeList, routerList, routertableList = f[1].split(
        '\n')[1:], f[2].split('\n')[1:], f[3].split('\n')[1:]
    nodeAux, routerAux, routertableAux = [], [], []
    for elem in nodeList:
        node = elem.split(',')
        if len(node) == 5:
            node = Node(node[0], node[1], node[2], node[3], node[4])
            nodeAux.append(node)
    
    for elem in routerList:
        router = elem.split(',')
        if len(router) > 2:
            name = router[0]
            num_ports = router[1]
            router = router[2:] 
            i = 0
            node_routers = []
            while i <len(router):
                nodeRouter = Node_router(router[i], router[i+1], router[i+2])
                node_routers.append(nodeRouter)
                i+=3
            router = Router(name, num_ports, node_routers)
            routerAux.append(router)

    for elem in routertableList:
        routertable = elem.split(',')
        if len(routertable) == 4:
            routertable = Routertable(
            routertable[0], routertable[1], routertable[2], routertable[3])
            routertableAux.append(routertable)
    
    return nodeAux, routerAux, routertableAux

def printTopology():
    global nodes
    global router
    global routertable
    print("Nodes")
    for elem in nodes:
        elem.printElem()
    print("")

    print("Router")
    for elem in router:
        elem.printElem()
    print("")

    print("Routertable")
    for elem in routertable:
        elem.printRoutertable()
    print("")

def ARPRequest(source, destiny):
    global nodes
    global router

    sourceNode = None
    destinyNode = None

    # procura informações sobre o nodo de origem e destino 
    # FIXME: -  o source pode ser um router
    for elem in nodes:
        if elem.name == source:
            sourceNode = elem
        elif elem.name == destiny:
            destinyNode = elem

    ip = sourceNode.ip_prefix.split("/")
    mask = int(ip[1])/8
    ip = ip[0].split(".")
    network , i = "", 0 
    while i < mask:
        network +=  ip[i] +'.'
        i += 1
    network =  network[:-1]

    # o ip destino é conhecido, possuem o mesma mascara
    if  network in destinyNode.ip_prefix:
        IP_dst = destinyNode.ip_prefix
    else:
    # o ip destino é desconhecido, não possuem a mesma mascara
        IP_dst = sourceNode.gateway      
    
    src_name, MAC_src, IP_src = sourceNode.name, sourceNode.mac, sourceNode.ip_prefix
    IP_dst = IP_dst.split("/")
    IP_src = IP_src.split("/")
    response = ARP_Request_response(src_name, MAC_src[-3:], ":FF", IP_dst[0], IP_src[0])
    response.printResponse()
    return response

def ARPReply(arp_request_response):
    global nodes
    global router
    response = None
    # IP_dst ser o destino
    for elem in nodes:
        ip = elem.ip_prefix.split("/")
        if ip[0] == arp_request_response.IP_dst:
            elem.arp_table.append((arp_request_response.IP_src, arp_request_response.MAC_src))
            response = ARP_Reply_response(elem.name, arp_request_response.src_name, elem.mac[-3:], arp_request_response.MAC_src[-3:], ip[0] )
            response.printResponse()
            break
    # IP_dst ser o gateway
    if response == None:
        for elem in router:
            node_routers = elem.node_routers 
            for port in node_routers:
                ip = port.ip_prefix.split("/")
                if ip[0] == arp_request_response.IP_dst:
                    elem.arp_table.append((arp_request_response.IP_src, arp_request_response.MAC_src))
                    response = ARP_Reply_response(elem.name, arp_request_response.src_name, port.mac[-3:], arp_request_response.MAC_src[-3:], ip[0] )
                    response.printResponse()
                    break
    # adiciona valores na arp_table de quem mandou o request
    if 'n' in response.dst_name:
        for elem in nodes:
            if elem.name == response.dst_name:
                elem.arp_table.append(
                    (response.IP_src, response.MAC_src))
                break
    elif 'r' in response.dst_name:
        for elem in router:
            if elem.name == response.dst_name:
                elem.arp_table.append(
                    (response.IP_src, response.MAC_src))
                break
    return(response)     


def ICMP_EchoRequest(src_name, dst_name, message, IP_source, IP_destiny):
    global nodes
    global router

    allElements = nodes+router
    sourceElem, destinyElem = None, None
    for elem in allElements:
        if elem.name == src_name:
            sourceElem = elem
        elif elem.name == dst_name:
            destinyElem = elem
    #ver MTU
    if 'r' in sourceElem.name:
        sourceElem.node_routers
        #verificar porta de saida
        MAC_src =  None
    if 'r' in destinyElem.name:
        sourceElem.node_routers
        #verificar porta de saida
        MAC_src = None
    # response = ICMP_Echo_Request(sourceElem.name, dst_name, MAC_src, MAC_dst, IP_source, IP_destiny, 8, 0, 0, message)
    response = ICMP_Echo_Request_response(sourceElem.name, dst_name, sourceElem.mac[-3:], sourceElem.mac[-3:], IP_source, IP_destiny, 8, 0, 0, message)
    response.printResponse()
    
    if IP_destiny in destinyElem.ip_prefix:
        #motar todas as respostas...
        print(response.dst_name + " rbox " + response.dst_name + ": Received " + response.data + ";\n")
        return True, response
    return False, response


def ICMP_EchoReply(echo_request_response):
    global nodes
    src_name = echo_request_response.dst_name
    dst_name = echo_request_response.src_name

    if 'r'in dst_name:
        #faz ARP REQUEST
        pass
    for elem in nodes:
        if elem.name == src_name:
            print(elem.arp_table)
    # self.MAC_src = MAC_src
    # self.MAC_dst = MAC_dst

    # response = ICMP_Echo_Reply_response( ,echo_request_response.IP_dst, echo_request_response.IP_src, 8, 0, 0, message)
    return

def main(source, destiny, message):
    global nodes
    global router
    global routertable
    for elem in nodes:
        if elem.name == source:
            IP_source = elem.ip_prefix
            ip = IP_source.split("/")
            IP_source = ip[0]
        elif elem.name == destiny:
            IP_destiny = elem.ip_prefix
            ip = IP_destiny.split("/")
            IP_destiny = ip[0]
    
    arp_request_response = ARPRequest(source, destiny)
    arp_reply_response   = ARPReply(arp_request_response)
    ended, echo_request_response = ICMP_EchoRequest(
        arp_reply_response.dst_name, arp_reply_response.src_name, message, IP_source, IP_destiny)
    IP_source,  IP_destiny =  "", ""
    if ended:
        ICMP_EchoReply(echo_request_response)
    # Pacotes ICMP Echo Request: <src_name> => <dst_name> : ETH (src=<MAC_src> dst =<MAC_dst>) 
    # IP (src=<IP_src> dst=<IP_dst> ttl=<TTL> mf=<mf_flag> off=<offset>) \n ICMP - Echo request (data=<msg>);
    # echo_request_response = ICMP_EchoRequest()


data = sys.argv
topologyFile, source, destiny, message = data[1], data[2], data[3], data[4]
nodes, router, routertable = readFile()

main(source, destiny, message)

# printTopology()  
# ARP Request
# ARP Reply 
# ICMP Echo Request
# ICMP Echo Reply
# ICMP Time Exceeded
# final do ICMP Echo Request
