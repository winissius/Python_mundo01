t=str('DESAFIO 08, CONVERSOR DE METROS PARA CENTRIMETROS E MILIMETROS')
print('{:=^105}'.format(t))

m=float(input('Digite o tamanho do membro, peça ou tacape\n'))
cm=m*100
mm=m*1000

print('O tamanho do seu membro é {}m\n em centimetros para se sentir melhor é {}cm\n em milímetros, se a coisa for realmente ruim é {}mm'.format(m,cm,mm))