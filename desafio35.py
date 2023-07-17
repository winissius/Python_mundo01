t = 'DESAFIO 35: CONDIÇÕES: TRES RETAS'
print('{:=^105}'.format(t))

r1 = float(input('Reta 01:'))
r2 = float(input('Reta 02:'))
r3 = float(input('Reta 03:'))

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    print('Forma um trinâgulo')

else:
    print('não forma um triângulo')