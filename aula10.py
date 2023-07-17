print('exemplo 01')

nome = str(input('Qual seu nome?: '))
if nome == 'Dedessa':
    print('Que nome lindo você tem!')
else:
    print('Interessante seu nome')
print('Bom dia, {}'.format(nome))

print('exemplo 02')
n1 = float(input('Insira a nota 01: '))
n2 = float(input('Insira a nota 02: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m>=6:
    print('Você está aprovado!')
else:
    print('Estude mais!')
print('PARABÉNS'if m>=6 else 'ESTUDE MAIS') #SIMPLIFICADO
if m>=10:
    print('Gênio!')