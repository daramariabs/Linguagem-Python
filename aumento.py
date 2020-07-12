__author__ = 'dara_'
salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000.00:
    p = 20.0
    aumento = (salario * p) / 100
    novo_sal = salario + aumento
elif salario <= 3000.00:
    p = 15
    aumento = (salario * p) / 100
    novo_sal = salario + aumento
elif salario <= 8000.00:
    p = 10
    aumento = (salario * p) / 100
    novo_sal = salario + aumento
else:
    p = 5
    aumento = (salario * p) / 100
    novo_sal = salario + aumento

print("Novo salario = R$","{:.2f}".format(novo_sal))
print("Aumento = R$","{:.2f}".format(aumento))
print("Porcentagem = ",p,"%")