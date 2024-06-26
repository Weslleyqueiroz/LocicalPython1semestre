# Desenvolva um programa que receba 3
#notas e calcule a média individual e da
#sala de 30 alunos. Calcule e mostre a
#maior e a menor média.
n1=float(input("Digite a primeira nota :"))
n2=float(input("Digite a segunda nota :"))
n3=float(input("Digite a terceira nota :"))
media=(n1+n2+n3)/3
media_total=0
cont=0
while cont<=30:
    print("A média individual dos alunos são: ",media)
    media_total=media_total+media/30
    cont=cont+1
print("A média da sala é :",media_total)

    