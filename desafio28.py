t = 'DESAFIO 28, CONDIÇÕES: JOGO DA ADIVINHAÇÃO'
print('{:=^105}'.format(t))

import random

n = random.randint(1, 5)
#print(n)
from time import sleep # função que faz o pc esperar x segundos para responder!

guess = int(input('Entre 1 e 5, escolha um número:\n'))

print('PROCESSANDO')
sleep(2)

if guess == n:
    print('Você ganhou!')
else:
    print('Você perdeu! Eu pensei no número {} e não no número {}!'.format(n,guess))



