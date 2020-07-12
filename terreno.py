__author__ = 'dara_'
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno:"))
metro_quad = float(input("Digite o valor do metro quadrado:"))

area_terreno = comprimento * largura
preco_terreno = metro_quad * area_terreno

print("AREA DO TERRENO =","{:.2f}".format(area_terreno))
print("PRECO DO TERRENO = ","{:.2f}".format(preco_terreno))