__author__ = 'dara_'
import math
preco_unitario = float(input("Preco unitario do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido:"))

valor_compra = preco_unitario * quantidade
troco = valor_compra - dinheiro
print("TROCO = ",math.fabs(troco))
