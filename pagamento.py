__author__ = 'dara_'
nome = input("Nome: ")
valor_hora = float(input("Valor por hora: "))
hora_trabalha = float(input("Horas trabalhadas: "))

pagamento = hora_trabalha * valor_hora
print("O pagamento para ",nome," deve ser R$",pagamento)