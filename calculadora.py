#coding utf-8

import time
import sys

def menu():
    while True:
        print("\n1 - Somar")
        print("2 - Diminuir")
        print("3 - Multiplicar")
        print("4 - Dividir")
        escolha = int(input("\n-> "))
        if escolha == 1:
            somar()
            break
            sys.exit()
        elif escolha == 2:
            diminuir()
            break
            sys.exit()
        elif escolha == 3:
            multiplicar()
            break
            sys.exit()
        elif escolha == 4:
            dividir()
            break
            sys.exit()
        else:
            print("\nOpção invalida")


def somar():   
    print("\nDigite o primeiro valor")
    x = eval(input("\n-> ")) 
    print("\nDigite o segundo valor")
    y = eval(input("\n-> "))
    z = x + y
    print("\nO resultado foi {}".format(z))
    	

def diminuir():
    print("\nDigite o primeiro valor")
    xx = eval(input("\n-> ")) 
    print("\nDigite o segundo valor")
    yy = eval(input("\n-> "))
    zz = xx - yy
    print("\nO resultado foi {}".format(zz))

def multiplicar():
    print("\nDigite o primeiro valor")
    xxx = eval(input("\n-> ")) 
    print("\nDigite o segundo valor")
    yyy = eval(input("\n-> "))
    zzz = xxx * yyy
    print("\nO resultado foi {}".format(zzz))

def dividir():
    print("\nDigite o primeiro valor")
    xxxx = eval(input("\n-> ")) 
    print("\nDigite o segundo valor")
    yyyy = eval(input("\n-> "))
    zzzz = xxxx / yyyy
    print("\nO resultado foi {}".format(zzzz))

menu()
