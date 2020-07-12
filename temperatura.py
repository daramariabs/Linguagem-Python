__author__ = 'dara_'
print("Voce vai digitar a temperatura em qual escala (C/F)?")
temperatura = input("")

if temperatura == "f":
    print("Digite a temperatura em Fahrenheit:")
    fa = float(input(""))
    celsius = 5 / 9 * (fa-32)
    print("Temperatura equivalente em Celsius:","{:.2f}".format(celsius))
else:
    print("Digite a temperatura em Celsius:")
    ce = float(input(""))
    farenait = ce * 9 / 5 + 32
    print("Temperatura equivalente em Fahrenheit:","{:.2f}".format(farenait))

