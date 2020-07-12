__author__ = 'dara_'

n = int(input("Quanto numeros voce vai digitar?"))
vet = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = float(input("Digite um numero:"))

maior = 0
for i in range(0,n):
    if vet[i] > maior :
        maior = vet[i]
        pos = i

print("MAIOR VALOR =",maior)
print("POSICAO DO MAIOR VALOR =",pos)