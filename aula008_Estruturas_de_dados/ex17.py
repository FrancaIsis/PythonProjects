import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: List Comprehensions [ ]')
print('='*70)

lista_numeros = [1, 2, 3, 4, 5]

# triplicar os valores
lista_nova_triplicada = []

for item in lista_numeros:
    lista_nova_triplicada.append(item * 3)

print('triplicar os valores: forma normal')
print(f'Lista triplicada: {lista_nova_triplicada}')
print()

# List Comprehensions
lista_nova_triplicada_2 = [item * 3 for item in lista_numeros]
print('triplicar os valores: List Comprehensions')
print(f'Lista triplicada: {lista_nova_triplicada_2}\n')
