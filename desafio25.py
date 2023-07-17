t='DESAFIO 25, VERIFICAÇÃO DOS SILVAS'
print('{:=^105}'.format(t))

n=input('Qual seu nome? ').strip()
n1=n.lower()
print('Você é membro da Família Silva {}'.format(n1.count('silva')==1))

print('Você é membro da família Silva? {}'.format('silva' in n.lower())) # saída melhor