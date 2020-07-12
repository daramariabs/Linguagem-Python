__author__ = 'dara_'

n = int(input("Quantos casos voce vai digitar?"))


for i in range (0,n):
    print("Digite os numeros:")
    x = float(input())
    y = float(input())
    z = float(input())
    media = (x * 2 + y * 3 + z * 5)/(2+3+5)
    print("MEDIA =","{:.1f}".format(media))