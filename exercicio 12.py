# Desenvolva um sistema que receba 2 notas e
#calcule a média final de cada aluno de uma sala
#com 60 alunos. Calcule também a média da sala.
nota1=float(input("Digite a primeira nota :"))
nota2=float(input("Digite a segunda nota :"))
media_aluno=(nota1+nota2)/2
cont=0
media_total=0
while cont<60:
    print("A media individual é de :",media_aluno)
    media_total=media_total+media_aluno
    cont=cont+1
media_sala=media_total/cont
print("A media da sala é de :",media_sala)