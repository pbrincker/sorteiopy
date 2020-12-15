#!/usr/bin/python
# 20140824

import random
import os

lista = []
escolha = "S"
sorteados = []
n = 1
#print("\n" * 100)
#print("\n")
#print ('SORTEIO EETAD')
print("\n" * os.get_terminal_size().lines)
while escolha == "S" :
    if len(lista)> 0:
        sorteado = (lista [ random.randrange ( len ( lista ))])
        sorteados.append(sorteado)
        print("\n" * os.get_terminal_size().lines)
        print ('SORTEIO EETAD:')
        print("\n")
        print ("O " + str(n) + "º ganhador(a) foi: " + sorteado)
        n+=1
        print("\n" * 20)
        print("\n")
        escolha = input("Deseja sortear mais um nome? [S/N]: ")
        #print("\n" * 130)
        if escolha == "Sim":
            escolha = "S"
        if escolha == "sim":
            escolha = "S"
        if escolha == "SIM":
            escolha = "S"
        if escolha == "s":
            escolha = "S"
        if escolha == "":
            escolha = "S"
        
        lista = [l for l in lista  if l != sorteado]
    else:
        escolha = "N"
    
else:
    x=0
    print("\n" * os.get_terminal_size().lines)
    print ("Confira a lista dos Sorteados: ")
    print("\n")
    while (x < len(sorteados)):
        print(str(x+1) +"º sorteado(a): "+ sorteados[x])
        x+=1
    print ("Parabéns a todos os ganhadores!!!")
    print("\n" * 20)
