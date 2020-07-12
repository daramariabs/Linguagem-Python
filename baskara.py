__author__ = 'dara_'
import math
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b:"))
c = float(input("Coeficiente c:"))

delta = b**2 - 4 * a * c
print("delta =",delta)
if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("X1 = ","{:.4f}".format(x1))
    print("X2 = ","{:.4f}".format(x2))
else:
    print("Esta equacao nao possui raizes reais")
