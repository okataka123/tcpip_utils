#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

host = "127.0.0.1"
port = 12345

# create socket object
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serversock.bind((host,port))

# wait for connection
serversock.listen(10)

print ('Waiting for connections...')
clientsock,client_address = serversock.accept()

rcvmsg = clientsock.recv(1024)
print(rcvmsg)
clientsock.close()
