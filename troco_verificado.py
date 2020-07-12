__author__ = 'dara_'
import math
preco_uni = float(input("Preco unitario do produto: R$"))
quantidade = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

pagar = preco_uni * quantidade

if dinheiro < pagar:
    fslta = dinheiro - pagar
    print("DINHEIRO INSUFICIENTE. FALTAM ",math.fabs(fslta)," REAIS")
else:
    troco = dinheiro - pagar
    print("TROCO = ",troco)