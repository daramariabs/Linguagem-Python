__author__ = 'dara_'
x = float(input("Valor de X:"))
y = float(input("Valor de Y:"))

if x > 0 and y > 0:
    print("QUADRANTE 1")
elif x < 0 and y > 0:
    print("QUADRANTE 2")
elif x < 0 and y < 0:
    print("QUADRANTE 3")
elif x > 0 and y < 0:
    print("QUADRANTE 4")
elif x != 0 and y == 0:
    print("Eixo X")
elif x == 0 and y != 0:
    print("Eixo Y")
else:
   print("ORIGEM")