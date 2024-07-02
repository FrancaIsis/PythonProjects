import os


os.system('cls')

# inicializa uma lista de exemplo
lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# solicita um usuario para inserir um indice para remover o elemento
indice = int(input('Digite o índice do elemento a ser removido (0-9): '))

# verifica se o indice esta dentro do intervalo válido da lista
if 0 <= indice < len(lista_numeros):
    # remove o elemento no índice especificado e exibe-o
    elemento_removido = lista_numeros.pop(indice)
    print(f'Elemento removido: {elemento_removido}')
    
else:
    print('Indice inválido!')

# exibe a lista resultante
print('Lista após remoção: ', lista_numeros)
