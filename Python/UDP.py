#!/usr/bin/env python
from socket import *
# TODO update for IPv6 support

class UDPServer:
    '''
    Ref:
        https://qiita.com/kashitaku/items/8db929ad6bf3a13e5e68
    '''
    def __init__(self):
        # TODO The following information should be read from the config file.
        srcIP = '127.0.0.1'
        srcPort = 22222
        self.srcAddr = (srcIP, srcPort)
        self.BUFSIZE = 1024 # ココがネックになるかも
        self.udpserversock = socket(AF_INET, SOCK_DGRAM)
        self.udpserversock.bind(self.srcAddr)

    def recv(self):
        while True:
            # always waiting to receive.
            data, addr = self.udpserversock.recvfrom(self.BUFSIZE)
            print(data)

class UDPClient:
    '''
    Ref:
        https://qiita.com/kashitaku/items/8db929ad6bf3a13e5e68
    '''
    def __init__(self):
        # TODO The following information should be read from the config file.
        srcIP = '127.0.0.1'
        srcPort = 11111
        self.srcAddr = (srcIP, srcPort)
        dstIP = '127.0.0.1'
        dstPort = 22222
        self.dstAddr = (dstIP, dstPort)
        self.udpclientsock = socket(AF_INET, SOCK_DGRAM)
        self.udpclientsock.bind(self.srcAddr)

    def send(self, data):
        # transform to binary
        data = data.encode('utf-8')
        self.udpclientsock.sendto(data, self.dstAddr)
