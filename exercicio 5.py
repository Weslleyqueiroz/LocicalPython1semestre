#As maçãs custam R$ 1,30 cada se forem compradas menos de
#uma dúzia, e R$ 1,00 se forem compradas pelo menos 12.
#Escreva um programa que leia o número de maçãs
#compradas, calcule e escreva o custo total da compra.


valor_maca=float(input("Digite quantas maças foram compradas: "))



if valor_maca<12:
    resultado=valor_maca*1.30
    print("O valor foi de :", resultado)
elif valor_maca>=12:
    resultado2=valor_maca*1
    print("O valor da compra foi de:", resultado2)
    
    