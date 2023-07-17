print('OPERADORES ARITMÉTICOS')

n1=int(input('digite um valor '))
n2=int(input('digite outro número '))

#strsoma=n1+n2
#sub=n1-n2
#mult=n1*n2
#div=n1/n2
#exp=n1**n2
#divint=n1//n2
#divrest=n1%n2

#print(soma)
#print(sub)
#print(mult)
#print(div)
#print(exp)
#print(divint)
#print(divrest)

print('CONFIGURAÇÕES DE STRING E ALINHAMENTO')
#n=input('Qual seu nome?')
#print('Prazer em te conhecer {:20}!'.format(n)) #:(operador de alinhamento)(número de caracteres)
#print('Prazer em te conhecer {:>20}!'.format(n)) #:(operador)(número de caracteres de alinhamento), alinhado a direita
#print('Prazer em te conhecer {:<20}!'.format(n)) #:(operador)(número de caracteres de alinhamento), alinhado a esquerda
#print('Prazer em te conhecer {:^20}!'.format(n)) #:(operador)(número de caracteres de alinhamento), alinhado a centralizado
#print('Prazer em te conhecer {:=^20}!'.format(n)) #:(OUTROS CARACTERES)(operador)(número de caracteres de alinhamento)

t='TESTES COM OPERADOERS'
print(' {:=^40}'.format(t))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {},\no produto é {}, \na divisão é {:.3f}, a divisão inteira é {} e o exponencial é {}'.format(s,m,d,di,e),end=' ')
#:.3f - trunca em 3 um float
print('manter tudo na mesma linha')