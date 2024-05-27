# Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra 'o' aparece
# e em que posição ela aparece pela primeira e última vez.

# importando as bibliotecas
import os


os.system('cls')

print('-' * 70)
print('Procurando a letra "O"')
print('=' * 70)

# inicializando variaveis
nome = ''
lista = ''
contador = 0


# entrada de dados
nome = input('Informe seu nome: ').lower().strip()

# tratamento dos dados

lista = list(nome)
contador = lista.count('o')

# em que posição a letra o aparece pela primeira vez
primeira_posicao = nome.find('o')
ultima_posicao = nome.rfind('o')

# saída de dados

print(f'O numero de vezes que a letra "o" aparece é {contador}')
print('')
print(f'A letra "o" aparece pela primeira vez na posição {primeira_posicao}')
print('')
print(f'A letra "o" aparece pela ultima vez na posição {ultima_posicao}')
print('')



