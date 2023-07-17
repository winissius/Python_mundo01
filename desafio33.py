t = 'DESAFIO 33: CONDIÇÕES: CLASSIFICADOR DE 03 NÚMEROS'
print('{:=^105}'.format(t))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))

if n2 > n1 and n2 > n3:
    print('O maior número é {}'.format(n2))

if n3 > n1 and n3 > n2:
    print('O maior número é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor número é {}'.format(n1))

if n2 < n3 and n2 < n1:
    print('O menor número é {}'.format(n2))

if n3 < n2 and n3 < n1:
    print('O menor número é {}'.format(n3))

print('\n\nOUTRA SOLUÇÃO\n\n')
#TESTANDO O MENOR, COM HIPÓSTESE SUGERIDA
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3 < n2:
    menor = n3
print('o menor é {}'.format(menor))
#TESTANDO O MAIOR
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('o maior é {}'.format(maior))
