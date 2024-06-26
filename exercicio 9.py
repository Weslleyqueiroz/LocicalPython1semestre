#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% 
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario=float(input("Digite o salário do colaborador :"))


if salario<=280:
    percentual_aumento = 20

elif salario<=700:
    percentual_aumento=15
   
elif salario<=1500:
    percentual_aumento=10
else:
    percentual_aumento=5
    
#calculo
valor_aumento=salario*percentual_aumento/100
novo_salario=salario+valor_aumento

print("O salario antes de ser reajustado é de:",salario)
print("O percentual de aumento é de :", percentual_aumento)
print("O valor do aumento é de :",valor_aumento)
print("O novo salario após reajuste é de :",novo_salario)

    
