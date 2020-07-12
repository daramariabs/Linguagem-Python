__author__ = 'dara_'

n = int(input("Informe um valor [Valor maximo possivel e 15]:"))
f=1
if n <= 15:
    for i in range(n,0,-1):
        f = f*i
print("FATORIAL = ",f)

