t=str('DESAFIO 10, CASA DE CAMBIO')
print('{:=^105}'.format(t))

r=float(input('Quantos mangos tem na carteira, meu consagrado?\nR$ '))
d=3.27

dr=r/d
dri=r//d
c=dr-dri

print('O senhor tem $ {:.2f}, ou seja: \n $ {} e ${:.2f} cents'.format(dr,dri,c))