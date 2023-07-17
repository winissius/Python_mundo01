t='DESAFIO 26, VERIFICAÇÃO DE LETRA E POSIÇÃO'
print('{:=^105}'.format(t))

n=str(input('Qual sua graça? ')).strip().lower()
print('Seu nome contem {} letras A'.format(n.count('a')))
print('O primeiro A aparece na posição {}'.format((n.find('a')+1)))
print('O ultimo A aparece na posição {}'.format((n.rfind('a')+1)))