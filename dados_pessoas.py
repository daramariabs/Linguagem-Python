__author__ = 'dara_'

n = int(input("Quantas pessoas serao digitadas?"))
vet_altura = [0 for x in range(n)]
vet_genero = [0 for x in range(n)]

for i in range(0,n):
    print("Altura da",i+1,"pessoa:")
    vet_altura[i] = float(input())
    print("Genero da",i+1,"pessoa")
    vet_genero[i] = input()

#maior altura
maior = vet_altura[0]
for i in range(1,n):
    if vet_altura[i] > maior:
        maior = vet_altura[i]

#menor altura
menor = vet_altura[0]
for i in range(1,n):
    if vet_altura[i] < menor:
        menor = vet_altura[i]

#altura media das mulheres
soma = 0
cont_f = 0
for i in range(0,n):
    if vet_genero[i] == 'f':
        soma = soma + vet_altura[i]
        cont_f = cont_f + 1

media = soma / cont_f

#quantidade de homens
cont_m =  n - cont_f


print("Menor altura =",menor)
print("Maior altura =", maior)
print("Media das alturas das mulheres =","{:.2f}".format(media))
print("Numero de homens =",cont_m)


