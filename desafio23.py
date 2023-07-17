t='DESAFIO 23, DISCRIMINAÇÃO DE DÍGITOS'
print('{:=^105}'.format(t))

n=str(input('Digite um número de 0 a 9999  ' ))

print('Milhar {}'.format(n[0]))
print('Centena {}'.format(n[1]))
print('Dezena {}'.format(n[2]))
print('Unidade {}'.format(n[3]))