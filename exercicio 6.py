# Leia a velocidade máxima permitida em uma avenida e a
#velocidade com que o motorista estava dirigindo nela e
#calcule a multa que uma pessoa vai receber, sabendo que
#são pagos:
    
#50 reais se o motorista estiver ultrapassar em até 10km/h a
#velocidade permitida (ex.: velocidade máxima: 50km/h;
#motorista a 60km/h ou a 56km/h);

vel_max=int(input("Digite a velocidade maxima permetida :"))
vel_motorista=int(input("Digite a velocidade do motorista :"))
diferenca=vel_motorista-vel_max
multa=50
multa2=100
multa3=200

if diferenca<=0:
    print("Sem multa")
    
elif(diferenca<=10):
    print("Multa de :", multa)
    
elif(diferenca<=30):
    print("Multa de :", multa2)
    
else:
    
    print("Multa de: ", multa3)
    
    