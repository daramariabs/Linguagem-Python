__author__ = 'dara_'
print("Digite as tres distancias:")
tentativa1 = float(input(""))
tentativa2 = float(input(""))
tentativa3 = float(input(""))

if tentativa1 > tentativa2 and tentativa1 > tentativa3:
    maior = tentativa1
elif tentativa2 > tentativa3:
    maior = tentativa2
else:
    maior = tentativa3

print("MAIOR DISTANCIA = ",maior)