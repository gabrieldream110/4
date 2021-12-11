# Faça um programa que mostre a tabuada de varios numeros, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado
# for negativo:
s = 0
n = 0
cont = 0
while True:
    n = int(input('Digite um valor para exibir sua tabuada (Digite -1 para encerrar):'))
    s += 1
    if n == -1:
        break
    for c in range(1,11):
        print(f'{n} x {s} = {n * s}')
    cont += 1
    if cont == 10:
        break
