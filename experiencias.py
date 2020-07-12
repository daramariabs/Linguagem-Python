__author__ = 'dara_'

n = int(input("Quantos casos de teste serao digitados?"))

c = 0
s = 0
r = 0
total_quant = 0

for i in range(0,n):
    quantidade = int(input("Quantidade de cobaias:"))
    cobaia = input("Tipo de cobaia:")
    if cobaia == 'c':
        c = c + quantidade
    elif cobaia == 's':
        s = s + quantidade
    else:
        r = r + quantidade
    total_quant = total_quant + quantidade

perc_c = (c * 100)/total_quant
perc_s = (s * 100)/total_quant
perc_r = (r * 100)/total_quant

print("RELATORIO FINAL:")
print("Total:",total_quant)
print("Total de coelhos:",c)
print("Total de sapos:",s)
print("Total de ratos:",r)
print("Percentual de coelhos:","{:.2f}".format(perc_c))
print("Percentual de sapos:","{:.2f}".format(perc_s))
print("Percentual de ratos:","{:.2f}".format(perc_r))