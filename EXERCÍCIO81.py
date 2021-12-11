# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a) Quantos números foram digitados;
# b) A lista de valores, ordenada de forma decrescente;
# c) Se o valor 5 foi digitado e está ou não na lista;

lista = []
r = ''
count = 0
countb = 0
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar S/N? ')).upper()
    lista.append(n)
    count += 1
    if n == 5:
        countb += 1
    if r == 'N':
        print('Fim')
        break
lista.sort(reverse=True)
print(f'Lista = {lista}')
print(f'\nNúmeros digitados para essa lista = {count}')
if 5 in lista:
    print(f'O valor 5 está na lista e foi digitado {countb} vezes no programa.')
