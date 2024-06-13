# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

import os


os.system('cls')

print('-'*70)
print('INSERINDO O NÚMERO FALTANTE')
print('='*70)

# criando a lista
lista = [1, 2, 3, 5, 6]

print(lista)

# solicitando ao usuario que informe o valor que está faltando
valor_faltante = input('Informe o valor que está faltando na lista acima: ')
posicao = int(
    input('Informe a posição em que esse valor deverá ser inserido: '))+1
