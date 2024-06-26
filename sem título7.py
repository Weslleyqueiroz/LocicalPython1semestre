#Escreva um algoritmo para ler o número total de eleitores de um município, o
#número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada
#um representa em relação ao total de eleitores.
total_eleitores=int(input("Digite o número total de eleitores :"))
votos_brancos=int(input("Digite o numero total de votos brancos: "))
votos_nulos=int(input("Digite o numero total de votos nulos: "))
votos_validos=int(input("Digite o numero total de votos validos: "))

print("O total de eleitores são: ",total_eleitores,"eleitores")
print("O total de votos brancos são: ",votos_brancos)
print("O total de votos nulos são: ",votos_nulos)
print("O total de votos validos são: ",votos_validos)

#calculo percentual
calculo_eleitores=(votos_brancos+votos_nulos+votos_validos*100)/total_eleitores
print("O percentual de total eleitores é: ", calculo_eleitores)