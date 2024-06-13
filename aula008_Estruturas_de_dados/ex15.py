import os


os.system('cls')

print('-'*70)
print('Saída com IN E NOT IN')
print('='*70)

# exemplo com in
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if (3 in lista_numeros):
    print(lista_numeros)
    posicao = lista_numeros.index(3)
    print(f'O numero 3 está na posição {posicao}')
else:
    print('O elemento não consta na listagem.')

# exemplo com not in
lista_nomes = ['john', 'jane', 'carol']

if ('Maria' not in lista_nomes):
    # antes
    print(lista_nomes)

    # não está na lista, acrescentar
    lista_nomes.append('Maria')

    print('\nO nome Maria foi adicionado.')
    print(lista_nomes)

print()
print('-'*70)
print('Fim do programa!')
print('='*70)
