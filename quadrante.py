__author__ = 'dara_'

print("Digite os valores das coordenadas X e Y:")
x = int(input())
y = int(input())

while x != 0 and y != 0 :
    if x > 0 and y > 0:
        print("QUADRANTE 1")
    elif x < 0 and y > 0 :
        print("QUADRANTE 2")
    elif x < 0 and y < 0 :
        print("QUADRANTE 3")
    else:
        print("QUADRANTE 4")
    print("Digite os valores das coordenadas X e Y:")
    x = int(input())
    y = int(input())
