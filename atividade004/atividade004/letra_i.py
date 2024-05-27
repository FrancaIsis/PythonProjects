# Faça um programa que receba o nome completo de uma pessoa e, em seguida, mostre o primeiro e o último nome.

# importando as bibliotecas
import os


os.system('cls')

print('-' * 70)
print('Primeiro e último')
print('=' * 70)

# inicializando variavel
nome = ''

# entrada de dados
nome = input('Digite seu nome completo: ').strip()
print('')

# tratamento de dados
lista = nome.split()

print(f'O primeiro nome digitado é: {lista[0]}')
print(f'O último nome digitado é {lista[-1]}')
print('')
