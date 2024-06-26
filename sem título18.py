# -*- coding: utf-8 -*-
def IMC (peso,altura):
    calculo_imc= peso/altura**2
    print("O calculo imc é :",calculo_imc)

    if calculo_imc<=18.5:
        print("Abaixo do normal")
    elif calculo_imc<=25:
        print("Normal")
    elif calculo_imc<30:
        print("Sobrepeso")
    elif calculo_imc<35:
        print("Obesidade grau I")
    elif calculo_imc<40:
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")
        
peso=float(input("Digite o seu peso :"))
altura=float(input("Digite a sua altura :"))

IMC(peso, altura)

