# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
s = 0
n = 0
cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:# Flag -> Interruptor do While infinito.
        break
    cont += 1
    s += n
print(f'A soma entre os {cont} números digitados é igual a {s}')
