t = str('DESAFIO 15, ALUGUEL DE CARROS')
print('{:=^105}'.format(t))

d = float(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km foram rodados? '))

a = d * 60 + 0.15 * km

print('O custo do aluguel do carro é R$ {:.2f}'.format(a))
