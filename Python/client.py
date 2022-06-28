#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

# server's ipadress
host = "127.0.0.1"
# server's port
port = 12345

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client.connect((host,port))
client.send(b"from python")
response = client.recv(4096)

print(response)
client.close()
