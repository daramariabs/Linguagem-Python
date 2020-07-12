__author__ = 'dara_'
import math
inicio = int(input("Hora inicial: "))
fim = int(input("Hora final:"))

if inicio == fim:
    duracao = 24
elif inicio > fim:
     duracao = ( 24 - inicio) + fim
else:
     duracao = inicio - fim

print("O JOGO DUROU ",math.fabs(duracao)," HORA(S)")