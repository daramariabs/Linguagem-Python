__author__ = 'dara_'

n = int(input("Quantos numeros voce vai digitar?"))
cont_d = 0
cont_f = 0

for i in range (0,n):
    x = int(input("Digite um numero:"))
    if x >= 10 and x <= 20:
        cont_d = cont_d + 1
    else:
        cont_f = cont_f + 1

print("DENTRO =",cont_d)
print("FORA =", cont_f)