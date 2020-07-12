__author__ = 'dara_'

n = int(input("Serao digitados dados de quantos produtos?"))
vet_nome = [0 for x in range(n)]
vet_compra = [0 for x in range(n)]
vet_venda = [0 for x  in range(n)]

for i in range(0,n):
    print("Produto",i+1,":")
    vet_nome[i] = input("Nome:")
    vet_compra[i] = float(input("Preco de compra:"))
    vet_venda[i] = float(input("Preco de venda:"))

#lucro percentuais
abaixo_dez = 0
entre_dez_vinte = 0
maior_vinte = 0
for i in range(0,n):
    perc_lucro = (( vet_venda[i] - vet_compra[i] )* 100) / vet_compra[i]
    if perc_lucro < 10:
        abaixo_dez = abaixo_dez + 1
    elif perc_lucro <= 20:
        entre_dez_vinte = entre_dez_vinte + 1
    else:
        maior_vinte = maior_vinte + 1

#valor total de compra e venda
tot_compra = 0
tot_venda = 0
for i in range(0,n):
    tot_compra = tot_compra + vet_compra[i]
    tot_venda = tot_venda + vet_venda[i]

#vlor total do lucro
lucro_total = tot_venda - tot_compra

print("RELATORIO:")
print("Lucro abaixo de 10%:",abaixo_dez)
print("Lucro entre 10% e 20%:",entre_dez_vinte)
print("Lucro acima de 20%:",maior_vinte)
print("Valor total de compra:","{:.2f}".format(tot_compra))
print("Valor total de venda:","{:.2f}".format(tot_venda))
print("Lucro total:","{:.2f}".format(lucro_total))