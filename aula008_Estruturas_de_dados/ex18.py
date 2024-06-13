import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: List Comprehensions [ ]')
print('='*70)

lista_numeros = [100, 200, 300, 500, 600]

# triplicar os valores
lista_com_juros = []

for item in lista_numeros:
    lista_com_juros.append(item + (item * .10))

print('Aplicar 10% de juros: forma normal')
print(f'Lista triplicada: {lista_com_juros}')
print()

# List Comprehensions
lista_com_juros_2 = [item + (item * .10) for item in lista_numeros]
print('Aplicar 10% de juros: List Comprehensions')
print(f'Lista triplicada: {lista_com_juros_2}')
