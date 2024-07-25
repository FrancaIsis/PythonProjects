# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Crie uma função que receba 2 listas: 
#- lista 1: nome, peso, idade
#- lista 2: John, 40, 1.8
#- Sua função deverá criar um dicionário contendo chave e valor utilizando como base essas duas listas. 
#  Depois, seu programa deverá imprimir esse dicionário utilizando uma estrutura de repetição for.

import os


os.system('cls')

print('-' * 70)
print('DICIONARIO')
print('=' * 70)

dicionario = {}

lista_chave = ['nome', 'peso', 'idade']
lista_valor = ['John', 40, 18]

def criar_dicionario(lista_chave, lista_valor):
    for chave, valor in zip(lista_chave, lista_valor):
        dicionario[chave]= valor
    return dicionario

dicionario_criado = criar_dicionario(lista_chave, lista_valor)

print(dicionario_criado)