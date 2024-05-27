# Faça um programa que leia o nome de uma pessoa e verifique se a 
# palavra 'Oliveira' está presente neste nome, mostrando True ou False

# importando bibliotecas

import os


os.system('cls')

print('-' * 70)
print('É OLIVEIRA OU NÃO??')
print('=' * 70)

# entrada de dados

nome = input('Digite o seu nome: ').title()
tipo = type(nome)
print(tipo)

# validação

#if tipo != str:

#    print('Valor inválido - digite um TEXTO!')
#else:
    # verificando se a palavra Oliveira esta contida no nome

print(f'Seu nome é {nome}')

if 'Oliveira' in nome:
    print(bool('Oliveira'))
else:
    print(bool())
