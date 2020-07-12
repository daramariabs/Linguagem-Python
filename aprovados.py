__author__ = 'dara_'

n = int(input("Quantos alunos serao digitados?"))
vet_nome = [0 for x in range(n)]
vet_nota1 = [0 for x in range(n)]
vet_nota2 = [0 for x in range(n)]

for i in range(0,n):
    print("Digite nome, primeira e segunda nota do",i+1," aluno:")
    vet_nome[i] = input()
    vet_nota1[i] = float(input())
    vet_nota2[i] = float(input())

print("Alunos aprovados:")
for i in range(0,n):
    media = (vet_nota1[i] + vet_nota2[i])/ 2
    if media >= 6:
        print(vet_nome[i])
