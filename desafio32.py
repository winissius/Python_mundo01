t = 'DESAFIO 32: CONDIÇÕES: ESSE ANO É BISSESTO?'
print('{:=^105}'.format(t))

ano = int(input('Qual ano deseja saber? Se deseja saber o ano atual digite 0: '))

from datetime import date

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
