# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre - os em uma lista,
# já na posição correta da inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
n = 0
maior = menor = 0

for x in range(0, 5):
    n = int(input('Digite um valor: '))
    lista.append(n)
print(f'\nLista = {lista}')
for c, v in enumerate(lista):
    if lista[3] > lista[4]:
        lista.append(lista[3])
        del lista[3]
    if lista[2] > lista[3]:
        lista.append(lista[2])
        del lista[2]
    if lista[1] > lista[2]:
        lista.append(lista[1])
        del lista[1]
    if lista[0] > lista[1]:
        lista.append(lista[0])
        del lista[0]
print(f'\nLista ordenada = {lista}')
