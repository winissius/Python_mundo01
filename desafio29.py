t = 'DESAFIO 29: CONDIÇÕES: RADAR DE VELOCIDADE'
print('{:=^105}'.format(t))

#import random
from random import uniform

v = uniform(60, 140) #retorna um número randomico float
print('Velocidade do veículo ao cruzar o radar: {:.2f}km/h'.format(v))

if v>80:
    print('Você foi multado!')
    print('Sua multa será: R${:.2f}'.format(7 * (v - 80)))
else:
    print('Continue viajando de forma segura!')

