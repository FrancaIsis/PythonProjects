import os


os.system('cls')

# solicitar ao usuario a quantidade de elementos na tupla
numero_elementos = int(input('Quantos elementos na tupla?'))

# inicializar uma lista vazia para armazenar elementos
elementos = []

# estrutura de repetição para obter os elementos do usuario
for i in range(numero_elementos):
    while True:
        valor = input(f'Digite o valor {i + 1}: ')
        if valor.isdigit():  # verifica se a entrada é um numero
            elementos.append(int(valor))
            break
        else:
            print('Entrada invalida. Digite um número.')

# converter a lista para uma tupla
tupla = tuple(elementos)

print('-'*70)
# exibir a tupla criada
print(f'Tupla criada: {tupla}')
print('-'*70)

# estrutura de repetição para permitir multiplas operações até que o usuario deseje sair
while True:
    # condicinal para verificar a presença de um numero especifico
    valor = int(input('Verificar se o numero na Tupla: '))
    if valor in tupla:
        print(f'O numero {valor} está na tupla.')
        # contar quantas vezes o numero aparece
        contagem = tupla.count(valor)
        print(f'O numero {valor} aparece {contagem} vez(es).')
        # encontrar o indice da primeira ocorrencia
        indice = tupla.index(valor)
        print(f'A 1° ocorrência de {valor} está no índice {indice}.')
    else:
        print(f'O número {valor} não está na tupla')

    # perguntar ao usuario se deseja realizar outra operação ou sair

    continuar = input('Deseja continuar? (s/n): ').lower()
    if continuar != 's':
        print('Encerrando o programa. Até mais!')
        break

    print('-'*70)
    print('Fim do programa!')
    print()
