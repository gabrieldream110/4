# Desafio 62: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Progressão Aritmética Melhorada')
print('-='*20)
a1     = int(input('Primeiro Termo: '))
r      = int(input('Razão da Progressão: '))
cont   = 1
t      = a1
mais   = 10
#total de termos da PA inicial
total  = 0
#acima temos quantos termos serão adicionados pelo usuário

while mais != 0:
    total += mais
    #contador de todos os termos no começo da programação.
    #total de termos adicionais for igual a zero, o programa encerra.
    while cont <= total:
        #Aqui o contador precisa ser igual ou menor ao total de termos calculados anteriormente.
        print('{} -> '.format(t),end='')
        t += r
        cont += 1
    #Aqui, após o programa exibir os 10 primeiros termos, é feita uma pausa para receber mais termos,
    #se o usuário desejar.
    print('\nPAUSA')
    mais = int(input('\nQuantos termos quer adicionar à progressão? R:  '))
    #após o usuário dar o input para exibir os termos adicionais, o programa vai repetir os comandos anteriores.
print('Progressão finalizada com {} termos mostrados no total.'.format(total))