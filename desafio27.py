t='DESAFIO 27, ANALISE DE NOME'
print('{:=^105}'.format(t))

n=str(input('Qual seu nome?  ')).strip()
n1=n.split()

print('seu primeiro nome é {}'.format(n1[0]))
print('seu ultimo nome é {}'.format(n1[len(n1)-1]))