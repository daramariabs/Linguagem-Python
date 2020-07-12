__author__ = 'dara_'

n = int(input("Quantas pessoas serao digitadas?"))
vet_nome = [0 for x in range(n)]
vet_idade = [0 for x in range(n)]
vet_altura = [0 for x in range(n)]

for i in range(0,n):
    print("Dados da ",i+1," pessoa:")
    vet_nome[i] = input("Nome:")
    vet_idade[i] = int(input("Idade:"))
    vet_altura[i] = float(input("Altura:"))

soma = 0
for i in range(0,n):
    soma = soma + vet_altura[i]

media = soma / n
print("Altura media:","{:.2f}".format(media))

cont_idade = 0
for i in range(0,n):
    if vet_idade[i] < 16:
        cont_idade = cont_idade + 1

perc_idade = (cont_idade * 100) / n
print("Pessoas com menos de 16 anos:","{:.2f}".format(perc_idade),"%")

#imprimindo os nomes dos menores de 16 anos
for i in range(0,n):
    if vet_idade[i] < 16:
        print(vet_nome[i])

