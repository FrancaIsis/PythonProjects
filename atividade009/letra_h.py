# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Faça um programa para ler o dicionário nomes = {‘nome’: ’John, ‘idade’: 40, ‘peso’: 80, ‘altura’: 1.70}.
# Em seguida realize as seguintes ações:
# - Listar chaves e valores com laço - Deletar o peso
# - Listar novamente chaves e valores - mostrar o nome e altura

import os


os.system('cls')

print('-' * 70)
print('DICIONÁRIO')
print('=' * 70)

nomes = {'nome': 'John', 'idade': 40, 'peso': 80, 'altura': 1.70}

#mostrando os valores com laço
for chave, valor in nomes.items():
    print(f'{chave}:{valor}')

# deletando o peso
del nomes['peso']
print('-'*70)

#mostrando apenas nome e altura
for chave, valor in nomes.items():
    if chave == 'idade':
        continue
    print(f'{chave}:{valor}')