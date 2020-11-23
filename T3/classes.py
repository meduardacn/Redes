class Node:
    def __init__(self, name, mac, ip_prefix, mtu, gateway):
        self.name = name
        self.mac = mac
        self.ip_prefix = ip_prefix
        self.mtu = mtu
        self.gateway = gateway
        self.arp_table = []

    def printElem(self):
        print("<" + self.name + "><" + str(self.mac) + "><" + str(self.ip_prefix) + "><" + str(self.mtu) + "><" + str(self.gateway) + ">")
        for elem in self.arp_table:
            print(elem)

class Router:
    def __init__(self, name, num_ports, node_routers):
        self.name = name
        self.num_ports = num_ports
        self.node_routers = node_routers
        self.arp_table = []

    def printElem(self):
        print("<" + self.name + "><" + str(self.num_ports) + ">")
        for elem in self.node_routers:
              elem.printNode_router()
        for elem in self.arp_table:
            print(elem)

class Node_router:
    def __init__(self, mac, ip_prefix, mtu):
        self.mac = mac
        self.ip_prefix = ip_prefix
        self.mtu = mtu

    def printNode_router(self):
        print( "<" + self.mac + "><" + str(self.ip_prefix) + "><" + str(self.mtu) + ">")

class Routertable:
    def __init__(self, name, dest_prefix, nexthop ,port):
        self.name = name
        self.dest_prefix = dest_prefix
        self.nexthop = nexthop
        self.port = port

    def printRoutertable(self):
        print("<" + self.name + "><" + str(self.dest_prefix) + "><" + str(self.nexthop) +
              "><" + str(self.port) + ">")

#-------------------------------------------
class ARP_Request_response:
    def __init__(self, src_name, MAC_src, MAC_dst, IP_dst, IP_src):
        self.src_name = src_name
        self.MAC_src  = MAC_src
        self.MAC_dst  = MAC_dst
        self.IP_dst   = IP_dst
        self.IP_src    = IP_src
    def printResponse(self):
        print(self.src_name + " box " + self.src_name + " : ETH (src=" + self.MAC_src +
              " dst=:FF) \\n ARP - Who has " + self.IP_dst + "? Tell " + self.IP_src + ";")

class ARP_Reply_response:
    def __init__(self, src_name, dst_name, MAC_src, MAC_dst, IP_src):
        self.src_name = src_name
        self.dst_name = dst_name
        self.MAC_src = MAC_src
        self.MAC_dst = MAC_dst
        self.IP_src = IP_src

    def printResponse(self):
        print(self.src_name + " => " + self.dst_name + " : ETH (src=" + self.MAC_src + " dst=" + self.MAC_dst +
              ") \\n ARP - " + self.IP_src + " is at " + self.MAC_src + ";")

class ICMP_Echo_Request_response:
    def __init__(self, src_name, dst_name, MAC_src, MAC_dst, IP_src, IP_dst, TTL, mf_flag, offset, data):
        self.src_name = src_name
        self.dst_name = dst_name
        self.MAC_src = MAC_src
        self.MAC_dst = MAC_dst
        self.IP_src = IP_src
        self.IP_dst = IP_dst
        self.TTL = TTL
        self.mf_flag = mf_flag
        self.offset = offset
        self.data = data

    def printResponse(self):
        print(self.src_name + " => " + self.dst_name + " : ETH (src=" + self.MAC_src + " dst=" + self.MAC_dst + ") \\n IP (src=" + self.IP_src + " dst=" + self.IP_dst + " ttl=" + str(self.TTL) +  " mf="+ str(self.mf_flag) + " off=" + str(self.offset) + ") \\n ICMP - Echo request (data=" + self.data + "); ")

class ICMP_Echo_Reply_response:
    def __init__(self, src_name, dst_name, MAC_src, MAC_dst, IP_src, IP_dst, TTL, mf_flag, offset, data):
        self.src_name = src_name
        self.dst_name = dst_name
        self.MAC_src = MAC_src
        self.MAC_dst = MAC_dst
        self.IP_src = IP_src
        self.IP_dst = IP_dst
        self.TTL = TTL
        self.mf_flag = mf_flag
        self.offset = offset
        self.data = data

    def printResponse(self):
        print(self.src_name + " => " + self.dst_name + " : ETH (src=" + self.MAC_src + " dst=" + self.MAC_dst +
              ") \\n IP (src=" + self.IP_src + " dst=" + self.IP_dst + " ttl=" + str(self.TTL) + " mf=" + str(self.mf_flag) + " off=" + str(self.offset) +
              ") \\n ICMP - Echo reply (data=" + self.data + "); ")