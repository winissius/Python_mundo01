t = str('DESAFIO 16, PARTE INTEIRA DE NÚMERO REAL')
print('{:=^105}'.format(t))

from math import trunc
n=float(input('Digite um número real '))

print('O número digitado foi {}, a parte inteira dele é {}'.format(n,(trunc(n))))
