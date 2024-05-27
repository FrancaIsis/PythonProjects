# Faça um programa que solicite separadamente o nome, o nome do meio e o sobrenome de uma pessoa. 
# Em seguida, imprima o nome completo.

# importando bibliotecas

import os


os.system('cls')

print('-' * 70)
print('Nomes')
print('=' * 70)

# inicializando variaveis

nome = ''
nome_do_meio = ''
sobrenome = ''

# entrada de dados

nome = input('Digite o seu primeiro nome: ').strip().capitalize()
nome_do_meio = input('Digite seu nome do meio: ').strip()
sobrenome = input('Digite seu sobrenome: ').strip().capitalize()

# criando uma lista para usar a função join

lista = [nome, nome_do_meio, sobrenome]
juncao = ' '.join(lista)

# saída de dados

print(f' Seu nome completo é: {juncao}')



