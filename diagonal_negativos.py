__author__ = 'dara_'

n = int(input("Qual a ordem da matriz?"))
mat = [[0 for x in range(n)] for x in range(n)]

for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]:"))

#diagonal principal
print("DIAGONAL PRINCIPAL:")
for i in range(0,n):
    for j in range(0,n):
        if i == j:
            print(mat[i][j],"",end="")
print()

#valores negativos na matriz
qtd_negativo = 0
for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] < 0:
            qtd_negativo = qtd_negativo + 1

print("QUANTIDADE DE NEGATIVOS =",qtd_negativo)