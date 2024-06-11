import os


os.system('cls')

# lista original
lista = [1, 2, 3, 4]

# pedindo ao usuario para fornecer a
# posição e o elemnto a ser inserido
posicao = int(input('Posição onde deseja inserir o elemento: '))
elemento = input('Elemento a ser inserido: ')

# verificando se a posição fornecida pelo usuario é valida
if posicao >= 0 and posicao <= len(lista):
    # inserindo o elemento na lista na posição especificada pelo usuario
    lista.insert(posicao, elemento)
    print('Lista após a inserção: ', lista)
else:
    print(f'Posição fora do intervalo 0, {len(lista)}')
