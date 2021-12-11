# Desafio 62: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Progressão Aritmética Melhorada')
print('-='*20)
primeiro = int(input('Primeiro Termo: '))
razao    = int(input('Razão: '))
cont     = 1
termo    = primeiro
total    = 0
mais     = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{}->'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))