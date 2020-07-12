__author__ = 'dara_'

n = int(input("Quantos numeros voce vai digitar?"))

for i in range (0,n):
    v = int(input("Digite um numero:"))
    if v == 0:
        print("NULO")
    elif v > 0:
        if v % 2 == 0:
            print("PAR POSITIVO")
        else:
            print("IMPAR POSITIVO")
    else:
        if v % 2 == 0:
            print("PAR NEGATIVO")
        else:
            print("IMPAR NEGATIVO")
