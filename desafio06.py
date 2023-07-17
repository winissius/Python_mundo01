t=str('DESAFIO 06, DOBRO, TRIPLO E RAIZ QUADRADA')
print('{:=^105}'.format(t))

n=int(input('DIGITE UM NÚMERO, POR GENTILEZA, MEU CONSGRADO\n'))
d=2*n
r=n**(1/2)

print('Seu número é {}\n o dobro do seu número é {}\n a raiz quadrada do seu número é {:.3f}'.format(n,d,r))