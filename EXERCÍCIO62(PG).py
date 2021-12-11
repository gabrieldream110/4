a1  = int(input('Digite o valor do primeiro termo de uma PA: '))
r   = int(input('Digite o valor da razão dessa PA: '))
n   = int(input('Quantos termos você quer ver a partir do início? '))
t   = r * (n -1)
an  = a1 + ((n - 1) * r)
x   = 0
print('Para uma progressão aritmética, com os valores abaixo: \n'
      'Primeiro Termo: {}\n'
      'Razão da Progressão: {}\n'
      'Número de Termos a ser exibido na tela: {}\n'
      'Temos esta PA:\n'.format(a1,r,n))
print(a1, end=' ')
while a1 <= an:
    a1 *= r
    print(a1, end=' ')
