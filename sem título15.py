# -*- coding: utf-8 -*-

cont=0
num = int(input("Entre com um numero :"))

while num!=0:
    print("numero positvo")
    if num>0:
        print("esse número é positivo",num)
        num = int(input("digite outro número :"))
    
    elif num<0:
        print("esse número é negativo", num)
        num = int(input("digite outro número :"))
        
    else:
        print("Digite um número. 0 para encerrar :",num)
        num = int(input("digite outro número :"))
        cont=cont + 1
print("loop encerrado")

    
   

