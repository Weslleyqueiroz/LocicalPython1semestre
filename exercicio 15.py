# -*- coding: utf-8 -*-


nomes=[]
print("---Imprimindo a primeira lista---")
cont = 0
while cont<5:
    nome=str(input("Digite um nome :"))
    nomes.append(nome)
    cont=cont  + 1
print("---Imprimindo a segunda lista---")
print(nomes)
del(nomes[3])
print(nomes)