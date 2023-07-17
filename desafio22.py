t='DESAFIO 22, FORMATAÇÃO NOME'
print('{:=^105}'.format(t))

n=str(input('Qual sua graça? '))

print(n.upper())
print(n.lower())
n1=n.strip()
n2=n1.count(' ')
#print('a quantidade espaços é {}'.format(n2))
#print('a quantidade de letras iniciais é {}'.format(len(n1)))
#l=len(n1)-n2
print('A quantidade de letras é {}'.format((len(n1)-(n2))))

nomesplit=n1.split()
pnome=nomesplit[0]

print('Seu primeiro nome é {}, tendo {} letras'.format(pnome, len(pnome)))