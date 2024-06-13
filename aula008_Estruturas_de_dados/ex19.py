import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: List Comprehensions [ ]')
print('='*70)

lista_precos = [100, 200, 300, 500, 600]

# triplicar os valores
lista_com_juros = []

for valor in lista_precos:
    if valor < 300:
        lista_com_juros.append(valor + (valor * .10))

print('Aplicar juros em condicional: forma normal')
print(f'Lista triplicada: {lista_com_juros}')
print()

# List Comprehensions
lista_com_juros_2 = [valor + (valor * .10)
                     for valor in lista_precos if valor < 300]
print('Aplicar juros em condicional: List Comprehensions')
print(f'Lista triplicada: {lista_com_juros_2}\n')
