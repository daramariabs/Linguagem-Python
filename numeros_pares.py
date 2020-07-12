__author__ = 'dara_'

n= int(input("Quantos numeros voce vai digitar?"))
vet= [0 for x in range(n)]

for i in range(0,n):
    vet[i]= int(input("Digite um numero:"))

cont_par = 0
print("NUMEROS PARES:")
for i in range(0,n):
    if vet[i] % 2 == 0:
        print(vet[i],"",end="")
        cont_par= cont_par + 1
print()

print("QUANTIDADE DE PARES =",cont_par)