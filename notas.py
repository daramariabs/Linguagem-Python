__author__ = 'dara_'

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

nf = n1 + n2

if nf < 60.0:
    print("NOTA FINAL =","{:.1f}".format(nf))
    print("REPROVADO")
else:
    print("NOTA FINAL = ","{:.1f}".format(nf))

