__author__ = 'dara_'

print("Digite as idades:")
idade = int(input(""))

soma = 0
cont = 0
if idade > 0:
    while idade > 0:
        soma = soma + idade
        cont = cont + 1
        idade = int(input(""))
    media = soma / cont
    print("MEDIA = ","{:.2f}".format(media))
else:
    print("IMPOSSIVEL CALCULAR")




