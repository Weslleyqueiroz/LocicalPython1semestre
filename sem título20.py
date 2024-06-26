cont=0
num=float(input("Digite um número para a validação :"))

while num!=0:
    if num>0:
        print("Esse número é positivo!")
    elif num<0:
        print("Negativo!!")
       
    else:
        print("Esse número é ZERO! Digite 0 para encerrar :")
    num=float(input("Digite um número para a validação :"))
    cont= cont + 1
print("Programa encerrado!")
        