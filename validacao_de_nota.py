__author__ = 'dara_'

nota1 = float(input("Digite a primeira nota:"))

while nota1 < 0 or nota1 > 10 :
    nota1 = float(input("Nota invalida! Informe um nova nota:"))

nota2 = float(input("Informe a segunda nota:"))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota invalida! Informe um novo nota:"))

media = (nota1 + nota2) / 2

print("MEDIA =",media)

