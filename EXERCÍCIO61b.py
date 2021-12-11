# Desafio 61: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Progressão Aritmética')
print('-='* 11)
a1   = int(input('Primeiro termo: '))
r    = int(input('Razão: '))
cont = 1
t = a1

while cont <= 10:
    print('{} -> '.format(t),end='')
    t += r
    cont += 1
print('FIM!')