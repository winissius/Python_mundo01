t=str('DESAFIO 19, SORTEIO DE ALUNOS')
print('{:=^105}'.format(t))

import random

#a=random.randint(1,4)
a1=input('Primeiro Aluno: ')
a2=input('Segundo Aluno: ')
a3=input('Terceiro Aluno: ')
a4=input('Quarto Aluno: ')
c=a1,a2,a3,a4
b=[a1, a2, a3, a4]

print('{}'.format(random.choice(b)))
#print('{}'.format(a))