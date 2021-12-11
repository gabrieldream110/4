# Crie um programa onde o usuário pode digitar vários valores numéricos e cadastre - os em uma lista.
#1 Passo: Criar uma estrutura de repetição que aceite quantos valores o usuário desejar.
# Caso o número já exista lá dentro, ele não será adicionado.
#2 Passo: Criar uma condição aninhada para que, se o valor digitado for repetido, será removido.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
#3 Passo: Usar a função sorted(lista) para exibir os valores em ordem crescente.

lista = []
r = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print(f'O número {n} já foi digitado anteriormente e não será repetido.')
    r = str(input('->Quer continuar S/N? ')).upper()

    if r == 'N':
        print('\nFim')
        break
print(f'Lista digitada = {sorted(lista)}')