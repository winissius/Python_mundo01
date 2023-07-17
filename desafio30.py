t='DESAFIO 30: CONDIÇÕES: PAR OU IMPAR'
print('{:=^105}'.format(t))

n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print('Par')
else:
    print('Ímpar')