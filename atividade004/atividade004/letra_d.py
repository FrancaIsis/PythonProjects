# Faça um programa que leia uma frase e depois exiba na tela:
# A frase em minúsculas, a frase em maiúsculas, a quantidade de
# caracteres na frase e quantas letras tem a 2ª palavra na frase

# importando as bibliotecas

import os


os.system('cls')

print('-' * 70)
print('MANIPULAÇÃO DE STRINGS')
print('=' * 70)

# inicializando a variavel

frase = ''

# entrada de dados

frase = input('Digite uma frase qualquer: ')
lista = frase.split()


# manipulando a variavel

print(f'A frase digitada por você foi: {frase}')
print('-'*70)
print(f'Sua frase em letras minúsculas: {frase.lower()}')
print('-'*70)
print(f'Sua frase em letras maiúsculas: {frase.upper()}')
print('-'*70)
print(f'Sua frase tem {len(frase)} caracteres.')
print('-'*70)
print(f'A segunda palavra da frase tem {len(lista[1])} caracteres.')
