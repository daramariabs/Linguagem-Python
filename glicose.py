__author__ = 'dara_'
glicose = float(input("Medida da glicose: "))

if glicose <= 100:
    print("Classificacao: normal")
elif glicose <= 140:
    print("Classificacao: elevado")
else:
    print("Classificacao: diabetes")