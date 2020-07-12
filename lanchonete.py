__author__ = 'dara_'
print("| codigo | Preco  |")
print("|   1    | R$5.00 |")
print("|   2    | R$3.50 |")
print("|   3    | R$4.80 |")
print("|   4    | R$8.90 |")
print("|   5    | R$7.32 |")

codigo = int(input("Codigo do produto comprado: "))

if codigo < 6:
    quantidade = int(input("Quantidade comprada: "))
    if codigo == 1:
        pagar = 5.00 * quantidade
    elif codigo == 2:
        pagar = 3.50 * quantidade
    elif codigo == 3:
        pagar = 4.80 * quantidade
    elif codigo == 4:
        pagar = 8.90 * quantidade
    else:
        pagar = 7.32 * quantidade
    print("Valor a pagar: ","{:.2f}".format(pagar))
else:
    print("Codigo Invalido!")
