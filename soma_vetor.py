__author__ = 'dara_'

n = int(input("Quantos numeros voce vai digitar?"))
vet = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = float(input("Digite um numero:"))

print("VALORES = ",end ="")
for i in range(0,n):
    print(vet[i],"",end ="" )

print()

soma = 0
for i in range(0,n):
    soma = soma + vet[i]
print("SOMA = ","{:.2f}".format(soma))

media = soma / n
print("MEDIA =","{:.2f}".format(media))
