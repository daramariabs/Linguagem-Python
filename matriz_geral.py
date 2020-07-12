__author__ = 'dara_'
import math

n = int(input("Qual a ordem da matriz?"))

mat = [[0 for x in range(n)] for x in range(n)]

for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = float(input(f"Elemento [{i},{j}]:"))

#soma dos positivos
soma = 0
for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]
print("SOMA DOS POSITIVOS:",soma)

#escolhendo uma linha da matriz para imprimir
l = int(input("Escolha uma linha:"))

print("LINHA ESCOLHIDA:",end="")
for i in range(0,n):
        print(mat[l][i],"",end="")

print()

#escolhendo uma coluna da matriz para imprimir
c = int(input("Escolha uma coluna:"))

print("COLUNA ESCOLHIDA:",end="")
for i in range(0,n):
    print(mat[i][c],"",end="")

print()
print()

#imprimindo diagonal principal
print("DIAGONAL PRINCIPAL:",end="")
for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] > 0:
            if i == j:
                print(mat[i][j],"",end="")
print()
print()

#alterando matriz, elevando os nnumeros negativos ao quadrado
for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] < 0:
            mat[i][j] = math.pow(mat[i][j],2)

print("MATRIZ ALTERADA:")
for i in range(0,n):
    for j in range(0,n):
        print(f"{mat[i][j]:.2f}","",end="")
    print()