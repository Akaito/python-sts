#!/usr/bin/env python3

import socket

import sts.inetsocket


print('host')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 2049))  # host, port
s.listen(1)

conn, addr = s.accept()
print(addr, 'connected to host')
while True:
    data = conn.recv(1024)
    if not data:
        break
    print('Received', data)

conn.close()
