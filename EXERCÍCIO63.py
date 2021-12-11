# Desafio 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci.
print('-=' * 20)
print('Sequência de Fibonacci')
print('-=' * 20)

n = int(input('Quantos termos você quer acessar? '))
t1 = 0
t2 = 1
count = 3
print('{} -> {} -> '.format(t1,t2),end='')
while count <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3),end='')
    t1 = t2
    t2 = t3
    count += 1
print('FIM')
