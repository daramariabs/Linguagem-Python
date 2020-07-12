__author__ = 'dara_'
minutos = int(input("Digite a quantidade de minutos:"))

if minutos > 100:
    excedido = minutos - 100
    pagar = 50.00 + (excedido * 2.00)
    print("Valor a pagar: R$","{:.2f}".format(pagar))
else:
    print("Valor a pagar: R$ 50.00")
