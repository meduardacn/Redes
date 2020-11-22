import sys
from classes import Node
from classes import Router
from classes import Node_router
from classes import Routertable

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
        elem.printNode()
    print("")

    print("Router")
    for elem in router:
        elem.printRouter()
    print("")

    print("Routertable")
    for elem in routertable:
        elem.printRoutertable()
    print("")

def ARPRequest():
    global nodes
    global router
    global source
    global destiny
    sourceNode = None
    destinyNode = None
    # procura informações sobre o nodo de origem e destino
    for elem in nodes:
        if elem.name == source:
            sourceNode = elem
        elif elem.name == destiny:
            destinyNode = elem
    if sourceNode.gateway == destinyNode.gateway:
        # o ip destino é conhecido, possuem o mesmo gateway
        IP_dst = destinyNode.ip_prefix
    else:
        # o ip destino é desconhecido, não possuem o mesmo gateway
        IP_dst = sourceNode.gateway     
    
    src_name, MAC_src, IP_src = sourceNode.name, sourceNode.mac, sourceNode.ip_prefix
    IP_dst = IP_dst.split("/")
    IP_src = IP_src.split("/")
    ARPRequest = (src_name, MAC_src, IP_dst[0], IP_src[0])
    print(src_name + " box " + src_name + " : ETH (src=" + MAC_src[-3:] +
          " dst=:FF) \ n ARP - Who has " + IP_dst[0] + "? Tell " + IP_src[0] + ";\n")
    ARPReply(ARPRequest)

def ARPReply(ARPRequest):
    global nodes
    global router
    src_name = ARPRequest[0]
    MAC_src = ARPRequest[1]
    IP_dst = ARPRequest[2]

    # IP_dst ser o destino
    for elem in nodes:
        ip = elem.ip_prefix.split("/")
        if ip[0] == IP_dst:
            print(elem.name + " => " + src_name + " : ETH (src=" + elem.mac[-3:] + " dst=" + MAC_src[-3:] + 
            ") \ n ARP - " + ip[0] + " is at " + elem.mac[-3:] + ";\n")
            return 
    # IP_dst ser o gateway
    for elem in router:
        node_routers = elem.node_routers
        for port in node_routers:
            ip = port.ip_prefix.split("/")
            print(ip[0],IP_dst)
            if ip[0] == IP_dst:
                print(elem.name + " => " + src_name + " : ETH (src=" + port.mac[-3:] + " dst=" + MAC_src[-3:] +
                      ") \ n ARP - " + ip[0] + " is at " + port.mac[-3:] + ";\n")
                return

data = sys.argv
topologyFile, source, destiny, message = data[1], data[2], data[3], data[4]
nodes, router, routertable = readFile()
ARPRequest()

# printTopology()  
# ARP Request ok
# ARP Reply 
# ICMP Echo Request
# ICMP Echo Reply
# ICMP Time Exceeded
# final do ICMP Echo Request
