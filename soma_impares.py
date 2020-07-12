__author__ = 'dara_'

print("Digite dois numeros:")
x = int(input())
y = int(input())

soma = 0
if x > y:
    t = x
    x = y
    y = t

for i in range (x + 1,y):
    if i % 2 == 1:
        print(i)
        soma = soma + i


print("SOMA DOS IMPARES =",soma)