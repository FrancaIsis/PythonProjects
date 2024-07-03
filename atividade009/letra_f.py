# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Faça um programa que cadastra 5 tipos de vinho.
# Para os campos deste cadastro tome como referência
# nome do vinho, tipo, teor alcoólico e safra.

import os


os.system('cls')

print('-' * 70)
print('CATÁLOGO DE VINHOS')
print('=' * 70)

catalogo = {}
lista = []
opcao = ''

while opcao != 's':
    catalogo['Indice'] = input('Informe o codigo do vinho: ')
    catalogo['Nome'] = input('Informe o nome do vinho: ')
    catalogo['Tipo'] = input('Informe o tipo: ')
    catalogo['Teor'] = input('Informe o teor alcoolico: ')
    catalogo['Safra'] = input('Informe a safra: ')
    lista.append(catalogo.copy())
    opcao = input('Deseja sair? (s/n)').lower().strip()

print('='*70)

for elemento in lista:
    for chave, valor in elemento.items():
        print(f'{chave}:{valor}', end='\n')
    print('='*70)

