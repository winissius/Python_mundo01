t=str('DESAFIO 20, ORDEM DE APRESENTAÇÃO DE ALUNOS')
print('{:=^105}'.format(t))

import random

a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))

list = [a1, a2, a3, a4]
b = random.sample(list,k=4)

print('A ordem de apresentação é:\n{}'.format(b))