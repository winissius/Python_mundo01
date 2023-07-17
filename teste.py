'''l = []
c = -1
while True:
    r = 'k'
    n = (int(input('digite um valor: ')))
    c += 1
    if c == 0:
        l.append(n)
    else:
        if n in l:
            print('Não vou adicionar')
        else:
            l.append(n)
    while r not in 'SN':
        r = str(input('Continuar [S/N]')).upper().strip()
    if r == 'N':
        break
print(l)
'''
estado1 = {'uf': 'Rio de Janeiro', 'siga': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
