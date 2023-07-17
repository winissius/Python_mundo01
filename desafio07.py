t=str('DESAFIO 07, NOTAS DO ALUNO COM MÉDIA')
print('{:=^105}'.format(t))

n1=float(input('INSIRA A NOTA DO PRIMEIRO SEMESTRE\n'))
n2=float(input('INSIRA A NOTA DO SEGUNDO SEMESTRE\n'))

m=(n1+n2)/2

print('A nota d primeiro semestre foi {}\n A nota do segundo semestre foi {}\n A média do aluno foi {:.1f}'.format(n1,n2,m))
print('\nO aluno foi aprovado',m>=6)