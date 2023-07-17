t = 'DESAFIO 34: CONDIÇÕES: AUMENTO POR FAIXA SALARIAL'
print('{:=^105}'.format(t))

s=float(input('Informe o salario para ser reajustado: R$ '))

if s > 1250:
    print('Novo salario é R$ {:.2f}'.format(s*1.10))
else:
    print('Novo salario é R$ {:.2f}'.format(s*1.15))