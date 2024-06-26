import os

os.system('cls')
# criação do dicionario vazio
meu_dicionario = {}

while True:
    print('-'*70)
    # exibição do menu de opções
    print('\nMenu de opções:')
    print('1 - Adicionar um par chave-valor')
    print('2 - Mostrar o dicionario')
    print('3 - Mostrar o tamanho do dicionario')
    print('4 - Fazer uma cópia do dicionario')
    print('5 - Limpar o dicionario')
    print('6 - Sair')
    print('-'*70)

    # solicitação da escolha do usuario
    opcao = input('Escolha uma opção (1-6):')

    if opcao == '1':
        # Adiciona um novo par chave-valor ao dicionario
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}: {valor} adicionado.')

    elif opcao == '2':
        # exibe o dicionario atual
        print('Dicionario atual:', meu_dicionario)
    elif opcao == '3':
        # Mostra o tamanho do dicionario usando len()
        tamanho = len(meu_dicionario)
        print(f'O dicionario tem {tamanho} elementos')
    elif opcao == '4':
        # Cria uma copia do dicionario usando copy() e exibe a cópia
        copia_dicionario = meu_dicionario.copy()
        print('Cópia do dicionario:', copia_dicionario)
    elif opcao == '5':
        # Limpa o dicionario usando o clear()
        meu_dicionario.clear()
        print('Dicionario limpo.')
    elif opcao == '6':
        # Sai do programa
        print('Saindo do programa.')
        break
    else:
        # Mensagem para opção inválida
        print('Opção inválida. Tente novamente.')
