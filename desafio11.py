t=str('DESAFIO 11, QUANTIDADE DE TINTA')
print('{:=^105}'.format(t))

a=float(input('Qual a altura da sua parede? '))
l=float(input('Qual a larguda da sua parede? '))
r=2 #L/m²

ap=a*l
lt=float(ap/r)

print('A área da sua parede é {:.2f}m²\nO senhor terá de desenbolsar {:.3f} L de tinta'.format(ap,
                                                                                               lt))