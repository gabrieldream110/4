# Faça um programa que leia 5 valores numéricos e guarde - os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = 0
menor = 0

n = int(input('Quantos valores deseja adicionar na lista? '))

for x in range(0,n):
    lista.append(int(input('Digite um valor: ')))
    if x == 0:
        menor = maior = lista[x]
    else:
        if lista[x] > maior:
            maior = lista[x]
        if lista[x] < menor:
            menor = lista[x]


print(f'\nO valor maior {maior} está nas posições ',end='')
for c,v in enumerate(lista):
    if v == maior:
        print(f'{c}...',end='')
print(f'\nO valor menor {menor} está nas posições ',end='')
for c,v in enumerate(lista):
    if v == menor:
        print(f'{c}...',end='')
