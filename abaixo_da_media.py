__author__ = 'dara_'

n = int(input("Quantos elementos vai ter o vetor?"))
vet = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = float(input("Digite um numero:"))

soma = 0
for i in range(0,n):
    soma = soma + vet[i]

media = soma / n
print("MEDIA DO VETOR = ","{:.3f}".format(media))

print("ELEMENTOS ABAIXO DA MEDIA:")
for i in range(0,n):
    if vet[i] < media:
        print(vet[i])