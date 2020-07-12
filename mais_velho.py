__author__ = 'dara_'

n = int(input("Quantas pessoas voce vai digitar?"))
vet_nome = [0 for x in range(n)]
vet_idade = [0 for x in range(n)]

for i in range(0,n):
    print("Dados da",i+1,"pessoa")
    vet_nome[i] = input("Nome:")
    vet_idade[i] = int(input("Idade:"))

mais_velho = 0
for i in range(0,n):
    if vet_idade[i] > mais_velho:
        mais_velho = vet_idade[i]
        nome = vet_nome[i]

print("PESSOA MAIS VELHA:",nome)