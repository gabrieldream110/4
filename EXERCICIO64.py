# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
soma = 0
count = 0
print('-='*20)
print('Contador de números aleatórios')
print('-='*20)
print('\n*Para finalizar o programa digite 999*\n')
while n != 999:
    n = int(input('Digite um valor inteiro: '))
    if n != 999:
        soma += n
        count += 1
print('O somatório de todos os {} números digitados é igual a: {}'.format(count,soma))
