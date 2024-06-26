# -*- coding: utf-8 -*-
cont=0
media_total=0
maior_nota=0
menor_nota=0

while(cont<5):
    nota1=float(input("Digite a primeira nota: "))
    nota2=float(input("Digite a segunda nota: "))
    media=(nota1+nota2)/2
    total=media_total+media
    print("A média do aluno foi: ", media)
    if(cont ==0):
        menor_nota=media
        maior_nota=media
    if(media<menor_nota):
        menor_nota=media
    if(media>maior_nota):
        maior_nota=media
    cont=cont+1
mediageral=total/cont
print("A média da sala é de :",mediageral)
print("A menor nota da sala é de :",menor_nota)
print("A maior nota da sala é de :",maior_nota)


