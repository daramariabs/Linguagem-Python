__author__ = 'dara_'
distancia = float(input("Distancia percorrida: "))
combustivel = float(input("Combustivel gasto:"))

consumo = distancia / combustivel
print("Consumo medio = ","{:.3f}".format(consumo))