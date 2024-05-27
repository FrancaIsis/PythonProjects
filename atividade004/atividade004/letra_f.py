# Faça um programa que receba o nome completo de uma pessoa e, posteriormente, imprima esse nome separadamente.

#importando bibliotecas

import os


os.system('cls')

print('-'*70)
print('SEPARAÇÃO DE NOME')
print('='*70)

# INICIALIZANDO VARIAVEIS

nome = ''

# entrada de dados

nome = input('Digite seu nome: ')
lista = nome.split()


# processamento de dados

for i in lista:
    print(i)

print('-'*70)