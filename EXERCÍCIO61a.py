# Desafio 61: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
# Obs: CRIAREI VÁRIAS VERSÕES DESSE EXERCÍCIO COM O OBJETIVO DE ENTENDER A LÓGICA POR TRÁS DELE E EXECUTÁ - LO
# COM HABILIDADE, ENTENDENDO A MECÂNICA DELE.

print('Progressão Aritmética')
print('-='* 11)

a1    = int(input('Primeiro Termo: '))
r     = int(input('Razão da Progressão: '))
cont  = 1
#precisei criar um contator de operações repetitivas no início da operação para a estrutura não se repetir
#infinitamente
termo = a1

while cont <= 10:
    #O comando print deve sempre estar na primeira linha em uma equação como essa,
    #senão o comando contará os termos a partir do segundo termo, contando 10 após ele,
    #eliminando o primeiro termo.
    print('{} -> '.format(termo),end='')
    termo += r
    cont += 1
    #O contador acima vai só até 10, já que estabeleci para a estrutura de repetição
    #efetuar o comando até cont se igual a 10, aí parar a execução.
print('FIM!')