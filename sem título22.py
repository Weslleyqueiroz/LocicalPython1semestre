#Desenvolva um programa que trabalhe com vetores para armazenar nomes
#de alunos em uma turma. Realize operações como adição e remoção de um
#nome na lista. O usuário entrará com 20 nomes utilizando a função de
#adicionar em Vetores, ao final solicitar um índice para o usuário e exclui-lo do
#vetor.
nomes=[]
cont=0
while cont<5:
    alunos=str(input("Digite um nome de aluno :"))
    nomes.append(alunos)
    cont=cont+1
print(nomes)
indice=(int(input("Digite um indíce para deletar :")))
del(nomes[indice])
print(nomes)