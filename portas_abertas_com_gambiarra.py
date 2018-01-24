#coding utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = raw_input("IP: ")
porta = int(input("Porta: "))



try:
    s.connect((ip, porta))
    print("{} Aberta".format(porta))
except:
    print("{} Fechada".format(porta))
