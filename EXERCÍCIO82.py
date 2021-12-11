# Crie um programa que vair ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista2 = []
lista3 = []
r = ''

while True:
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar S/N? ')).upper()
    lista.append(n)
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)

    if r == 'N':
        print('Fim')
        break

print(f'\nLista original = {lista}')
print(f'Lista de números pares = {lista2}')
print(f'Lista de números ímpares = {lista3}')
