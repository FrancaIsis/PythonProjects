# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Faça um programa para criar um dicionário com 5 ferramentas.
# Depois,  imprima os valores e a quantidade de elementos do dicionário.

import os


os.system('cls')

print('-' * 70)
print('FERRAMENTAS')
print('=' * 70)

ferramentas = {}


for i in range(1,6):
    chave = i
    valor = input('Informe o nome da ferramenta: ')
    ferramentas[chave] = valor
    print('-'*70)

# mostrando os dados do dicionario
print('Lista de Ferramentas:\n')
print('='*70)
print(f'Você inseriu {len(ferramentas)} ferramentas:\n')
for chave, valor in ferramentas.items():
    print(f'{chave} - {valor}')

