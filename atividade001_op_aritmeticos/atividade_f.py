# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.
# importando a biblioteca OS que faz a interação com o SO
import os


# limpando dados do terminal
os.system('cls')

# inicializando as variáveis
numero = 0
dobro = 0
triplo = 0

# entrada de dados
print('-'*70)
print('DOBRO E TRIPLO')
print('-'*70)

numero = int(input('Informe um número: '))

# processamento de dados
dobro = numero * 2
triplo = numero * 3

# saída de dados
print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'O número digitado por você foi {numero}: \n'
      f'O dobro de {numero} é {dobro}\n'
      f'O triplo de {numero} é {triplo}')
print('')
