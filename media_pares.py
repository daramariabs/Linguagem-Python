__author__ = 'dara_'

n = int(input("Quantos elementos vai ter o vetor?"))
vet = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = int(input("Digite um numero:"))

soma = 0
for i in range(0,n):
    if vet[i] % 2 == 0:
        soma = soma + vet[i]

if soma > 0:
    media = soma / n
    print("MEDIA DOS PARES =","{:.1f}".format(media))
else:
    print("NENHUM NUMERO PAR")

