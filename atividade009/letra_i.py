# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Faça um programa para criar um dicionário com 4 elementos.
# Depois imprima a lista completa, delete o último elemento e mostre uma listagem nova.

import os


os.system('cls')

print('-' * 70)
print('DICIONARIO')
print('=' * 70)

dicionario = {}


while True:
    print('-'*70)
    print('\nMenu de opções:')
    print('1 - Criar dicionário')
    print('2 - Mostrar dicionário')
    print('3 - Deletar o último elemento: ')
    print('4 - Sair')
    print('-'*70)

    opcao = int(input('Digite o número correspondente à sua escolha: '))

    if opcao == 1:
        chave = input('Digite as chaves separadas por virgulas ').split(
            ',')  # transformando em lista
        valor = input('Informe o valor padrão para as chaves: ')
        dicionario = dict.fromkeys(chave, valor)
        print('Dicionario criado com sucesso.')

    if opcao == 2:
        for chave, valor in dicionario.items():
            print(f'{chave}:{valor}', end='\n')
        # print(dicionario)

    if opcao == 3:
        if dicionario:
            chave, valor = dicionario.popitem()
            print(f'Item removido {chave}:{valor}')
    
    if opcao == 4:
        print('Saindo do programa...')
        break
