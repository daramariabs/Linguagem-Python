__author__ = 'dara_'

m = int(input("Qual a quantidade de linhas da matriz?"))
n = int(input("Qual a quantidade de colunas da matriz?"))

mat = [[0 for x in range(n)] for x in range(m)]
vet = [0 for x in range(m)]

for i in range(0,m):
    print("Digite os elementos da",i+1 ,"linha:")
    for j in range(0,n):
        mat[i][j] = float(input())

#realizando a soma das linhas e atribuindo ao vetor
for i in range(0,m):
    soma = 0
    for j in range(0,n):
        soma = soma + mat[i][j]
    vet[i] = soma

print("VETOR GERADO:")
for i in range(0,m):
    print(vet[i])