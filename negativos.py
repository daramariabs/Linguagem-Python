__author__ = 'dara_'

n = int(input("QUantos numeros voce vai digitar ?"))
vet = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = int(input("Digite um numero:"))

print()

print("NUMEROS NEGATIVOS:")
for i in range(0,n):
    if vet[i] < 0:
        print(vet[i])
