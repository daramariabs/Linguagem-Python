__author__ = 'dara_'

x = int(input("Digite um numero inteiro:"))
c = 0
soma = 0
while x != 0 :
    if x % 2 == 0 :
        while c != 5:
            soma = soma + x
            x = x + 2
            c = c +1
    else:
        x = x + 1
        while c != 5 :
            soma = soma + x
            x = x + 2
            c = c + 1
    print("SOMA = ",soma)
    soma = 0
    c = 0
    x = int(input("Digite um numero inteiro:"))



