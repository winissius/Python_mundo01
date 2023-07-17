t = str('DESAFIO 17, CALCULO DA HIPOTENUSA')
print('{:=^105}'.format(t))

from math import sqrt,pow
ca=float(input('Qual é o cateto adjacente? '))
co=float(input('Qual é o cateto oposto? '))
h= sqrt(pow(ca,2)+pow(co,2))

print('A hipotenusa do triangulo retangulo com catetos {} e {} é {:.5f}'.format(ca,co,h))