# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa para criar um dicionário com 4 elementos.

import os


os.system('cls')

dicionario = {}

print('-'*70)
print('Dicionario de 4 elementos')
print('='*70)

for i in range(1, 5):
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    dicionario[chave] = valor
    print('-'*70)
    print(f'\n{i}° par {chave}:{valor} adicionado.')
    print('-'*70)


print(dicionario)
