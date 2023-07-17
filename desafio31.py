t='DESAFIO 31: CONDIÇÕES: CÁLCULADORA DE CUSTO DE VIAGEM'
print('{:=^105}'.format(t))

d=float(input('Qual a distância da viagem em km? '))

if d<=200:
    print('Sua passagem irá custar R${:.2f}'.format(d*0.5))
else:
    print('Sua passagem irá custar R${:.2f}'.format(d * 0.45))

print('OUTRA FORMA DE RESOLUÇÃO\n')
if d <= 200:
    p= d * 0.5
else:
    p = d * 0.45

print('Você está prestes a iniciar uma viagem de {} km e ela irá custar R${}'.format(d,p))