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


def mask(ip_prefix): 
    # if ip_prefix == "0.0.0.0/0":
    #     return "0.0.0.0"
    ip = ip_prefix.split("/")
    mask = int(ip[1])/8
    ip = ip[0].split(".")
    network, i = "", 0
    while i < mask:
        network += ip[i] + '.'
        i += 1
    return network[:-1]

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

    # o ip destino é conhecido, possuem o mesma mascara
    if mask(sourceNode.ip_prefix) in destinyNode.ip_prefix:
        IP_dst = destinyNode.ip_prefix
    else:
    # o ip destino é desconhecido, não possuem a mesma mascara
        IP_dst = sourceNode.gateway      
    
    src_name, MAC_src, IP_src = sourceNode.name, sourceNode.mac, sourceNode.ip_prefix
    IP_dst = IP_dst.split("/")
    IP_src = IP_src.split("/")
    response = ARP_Request_response(src_name, MAC_src, ":FF", IP_dst[0], IP_src[0])
    response.printResponse()
    return response

def ARPRequestRouter(routerName, port, echo_request_responses):
    global router
    global ttl
    routerElem = None

    for elem in router:
        if elem.name == routerName:
            routerElem = elem
    route = routerElem.node_routers[int(port)]  
    routeIP = route.ip_prefix.split("/")
    response = ARP_Request_response(
        routerName, route.mac, ":FF", echo_request_responses[0].IP_dst, routeIP[0])
    response.printResponse()
    ttl = 8
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
            response = ARP_Reply_response(elem.name, arp_request_response.src_name, elem.mac, arp_request_response.MAC_src, ip[0] )
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
                    response = ARP_Reply_response(elem.name, arp_request_response.src_name, port.mac, arp_request_response.MAC_src, ip[0] )
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

def ICMP_EchoRequest(src_name, dst_name, MAC_dst, message, IP_source, IP_destiny, port):
    global nodes
    global router
    global ttl

    allElements = nodes+router
    sourceElem, destinyElem, mtu, MAC_src ,= None, None, 0, 0
    for elem in allElements:
        if elem.name == src_name:
            sourceElem = elem
        elif elem.name == dst_name:
            destinyElem = elem
    if 'r' in sourceElem.name:
        #verificar porta de saida
        route = sourceElem.node_routers[int(port)]
        MAC_src = route.mac
    else:
        MAC_src = sourceElem.mac
    
    if 'r' in destinyElem.name:
        mtu = int(destinyElem.node_routers[0].mtu)
        MAC_src = sourceElem.mac
    else:
        mtu = int(destinyElem.mtu)

    responses ,response = [], None
    i = 0
    if len(message) >= mtu:
        while i < len(message):
            if i+mtu < len(message):
                mf = 1
            else:
                mf = 0
            response = ICMP_Echo_Request_response(sourceElem.name, destinyElem.name, MAC_src, MAC_dst, IP_source, IP_destiny, str(ttl), str(mf), str(i), str(message[i:i+mtu]))
            
            response.printResponse()
            responses.append(response)
            i += mtu 
    ttl -= 1
    if 'n' in destinyElem.name:
        if IP_destiny in destinyElem.ip_prefix:
            message = ""
            for elem in responses:
                message += elem.data
            print(dst_name + " rbox " + dst_name + " : Received " + message + ";")
            return True, responses
    return False, responses

def ICMP_EchoReply(echo_request_responses, IP_source):
    global nodes
    global router
    responses = []
    for elem in echo_request_responses:
        response = ICMP_Echo_Reply_response(elem.dst_name, elem.src_name, elem.MAC_dst, elem.MAC_src, 
                                            elem.IP_dst, elem.IP_src, elem.TTL, elem.mf_flag, elem.offset, elem.data)
        responses.append(response)
        response.printResponse()
    if 'n' in responses[0].dst_name:
        if IP_source in responses[0].IP_dst:
            message = ""
            for elem in responses:
                message += elem.data
            print(responses[0].dst_name + " rbox " + responses[0].dst_name +
                " : Received " + message + ";")
            return True, responses
    return False, responses


def ICMP_EchoReplyRouter(echo_reply_responses, IP_source):
    global nodes
    global router
    global ttl
    destElem, MAC_src = None, 0
    for elem in nodes:
        if echo_reply_responses[0].IP_dst in elem.ip_prefix:
            destElem = elem
            break
    for elem in router:
        if elem.name == echo_reply_responses[0].dst_name:
            for group in elem.node_routers:
                if mask(destElem.ip_prefix) in group.ip_prefix:
                    MAC_src = group.mac
                    break
    responses = []
    for elem in echo_reply_responses:
        for node in nodes:
            if elem.IP_dst in node.ip_prefix:
                response = ICMP_Echo_Reply_response(elem.dst_name, node.name, MAC_src, node.mac,
                                                                    elem.IP_src, elem.IP_dst, ttl, elem.mf_flag, elem.offset, elem.data)
                response.printResponse()
                responses.append(response)

    if IP_source in responses[0].IP_dst:
        message = ""
        for elem in responses:
            message += elem.data
        print(responses[0].dst_name + " rbox " + responses[0].dst_name +
              " : Received " + message + ";")

def main(source, destiny, message):
    global nodes
    global router
    global routertable
    IP_source,  IP_destiny = "", ""
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
    ended, echo_request_responses = ICMP_EchoRequest(
        arp_reply_response.dst_name, arp_reply_response.src_name, arp_reply_response.MAC_src, message, IP_source, IP_destiny,0)
    
    if ended:
        received, echo_reply_responses = ICMP_EchoReply(
            echo_request_responses, IP_source)
    else:
        resp = echo_request_responses[0]
        IP_dst = resp.IP_dst
        for group in routertable:
            if mask(group.dest_prefix) in IP_dst:
                arp_request_response = ARPRequestRouter(group.name, group.port, echo_request_responses)
                arp_reply_response = ARPReply(arp_request_response)
                for elem in echo_request_responses:
                    ended, echo_request_responses = ICMP_EchoRequest(
                        arp_reply_response.dst_name, arp_reply_response.src_name, arp_reply_response.MAC_src, message, IP_source, IP_destiny, group.port)
                    if ended:
                        received, echo_reply_responses = ICMP_EchoReply(echo_request_responses, IP_source)

                    ICMP_EchoReplyRouter(echo_reply_responses, IP_source)
                    return 
            
                    
data = sys.argv
topologyFile, source, destiny, message = data[1], data[2], data[3], data[4]
ttl = 8
print(data)
nodes, router, routertable = readFile()
main(source, destiny, message)

# printTopology()
