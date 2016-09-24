#!/usr/bin/env python3

import socket

import sts.inetmgr

program_name = 'TestProg'
build = 1


print('client')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 2049))

ss = sts.inetmgr.connect(s, 'SomeConntype', program_name, build)
ss.send('MyProtocol', 'MyCommand', body='some_data')

ss.detach_socket()

s.close()

