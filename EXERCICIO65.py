# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('Para somar digite -1:')
soma = 0
n = int(input('Digite um número: '))
n1 = n
continuar = str(input('Quer continuar? S/N' )).upper().strip()
count = 0
media = 0
maior = n
menor = n
while continuar == 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? S/N' )).upper().strip()
    if n > 0:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    #if n != -1:
    soma += n
    count += 1
    media = (soma + n1)/(count + 1)
print('A soma entre todos os {} valores é igual a {} \n'
      'A média entre eles é igual a {}\n'
      'O maior número digitado foi {}\n'
      'O menor número digitado foi {}'.format(count + 1,soma + n1,media,maior,menor))

