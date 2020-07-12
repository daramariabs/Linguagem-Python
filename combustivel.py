__author__ = 'dara_'

print("Codigo | descricao")
print("  1    | Alcool   ")
print("  2    | Gasolina ")
print("  3    | Diesel   ")
print("  4    | Fim      ")

cont_alcool = 0
cont_diesel = 0
cont_gasolina = 0

cod = int(input("Informe um codigo (1, 2, 3) ou 4 para parar:"))

while cod != 4:
    if cod == 1:
        cont_alcool = cont_alcool + 1
    elif cod == 2 :
        cont_gasolina = cont_gasolina + 1
    elif cod == 3:
        cont_diesel = cont_diesel + 1

    cod = int(input("Informe um codigo (1, 2, 3) ou 4 para parar:"))

print("MUITO OBRIGADA!")
print("ALCOOL =",cont_alcool)
print("GASOLINA =",cont_gasolina)
print("DIESEL =",cont_diesel)
