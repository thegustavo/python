#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.0.101", 22))
a = s.recv(1024)
s.send("gustavo")
a = s.recv(1024)
s.send("senha_censurada")
a = s.recv(1024)

print a


