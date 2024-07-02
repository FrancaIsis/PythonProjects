import os


os.system('cls')

print('-'*70)
print('Saída com FOR...ENUMERATE()')
print('='*70)

soma = 0

# cirando uma lista
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# percorrendo a lista com o enumerate()
# O comando enumerate adiciona um indice
# para cada valor de nossa lista
# start opcional, para não começar com o índice 0
# enumerate(listaNumeros, start = 1)

# para cada numero dentro da lista de numeros, enumere com um índice
for i, numero in enumerate(lista_numeros):
    soma += numero  # soma os numeros
    print(f'Indice: {i} = Número: {numero}')

print('-'*70)
print(f'A soma de todos os numeros é: {soma}')
print('Fim do programa!')
print('-'*70)
