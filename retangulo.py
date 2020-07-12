__author__ = 'dara_'
import math
base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo:"))

area = base * altura
perimetro = (base * 2) + (altura * 2)
diagonal = math.sqrt(base**2 + altura**2)

print("AREA = ","{:.2f}".format(area))
print("PERIMENTRO = ","{:.2f}".format(perimetro))
print("DIAGONAL = ","{:.2f}".format(diagonal))
