class Node:
    def __init__(self, name, mac, ip_prefix, mtu, gateway):
        self.name = name
        self.mac = mac
        self.ip_prefix = ip_prefix
        self.mtu = mtu
        self.gateway = gateway

    def printNode(self):
        print("<" + self.name + "><" + str(self.mac) + "><" + str(self.ip_prefix) + "><" + str(self.mtu) + "><" + str(self.gateway) + ">")


class Router:
    def __init__(self, name, num_ports, node_routers):
        self.name = name
        self.num_ports = num_ports
        self.node_routers = node_routers

    def printRouter(self):
        print("<" + self.name + "><" + str(self.num_ports) + ">")
        for elem in self.node_routers:
              elem.printNode_router()

class Node_router:
    def __init__(self, mac, ip_prefix, mtu):
        self.mac = mac
        self.ip_prefix = ip_prefix
        self.mtu = mtu

    def printNode_router(self):
        print( "<" + self.mac + "><" + str(self.ip_prefix) + "><" + str(self.mtu) + ">")

class Routertable(object):
    def __init__(self, name, dest_prefix, nexthop ,port):
        self.name = name
        self.dest_prefix = dest_prefix
        self.nexthop = nexthop
        self.port = port

    def printRoutertable(self):
        print("<" + self.name + "><" + str(self.dest_prefix) + "><" + str(self.nexthop) +
              "><" + str(self.port) + ">")
