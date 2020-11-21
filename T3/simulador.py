import sys
from classes import Node
from classes import Router
from classes import Node_router
from classes import Routertable

def readFile(txt):
    f = open(txt, 'r')
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
                nodeRouter = Node_router(router[i], router[i], router[i+2])
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

def printTopology(node, router, routertable):
    print("Nodes")
    for elem in node:
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

data = sys.argv
topologyFile, source, destiny, message = data[1], data[2], data[3], data[4]
node, router, routertable = readFile(topologyFile)
printTopology(node, router, routertable)
