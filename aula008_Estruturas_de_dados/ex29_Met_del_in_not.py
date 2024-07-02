import os


os.system('cls')

# Inicialização do dicionario de contatos
agenda = {
    'Jojo': '99196-3030',
    'Dio': '99196-5050',
    'Jolyne': '99196-6060',
    'Lisa Lisa': '99196-8080',
    'Zeze': '99196-9090',
    'Suzie Q': '99196-0000'
}

while True:
    os.system('cls')
    print('-'*70)
    print('\nAgenda de Contatos:')
    for nome, telefone in agenda.items():
        print(f'{nome}:{telefone}')
    print('='*70)

    # Primeiro teste: erificar se Jojo está no dicionario
    if 'Jojo' in agenda:
        print('Primeiro teste: verificando se Jojo está no Dicionário')
        print('VERDADEIRO! Jojo está no dicionario')
    else:
        print('FALSO! Jojo não está no dicionário')

    print()

    # segundo teste: verificar se 'Jhon' não está no dicionário
    if 'John' not in agenda:
        print('Segundo teste: verificando se John não está no dicionario')
        print('VERDADEIRO! John não está no dicionário')
    else:
        print('FALSO! John está no dicionário')

    print('-'*70)
    print()
    print('-'*70)
    print('Menu de opções: ')
    print('1 - Adicionar um contato.')
    print('2 - Remover um contato')
    print('3 - Verificar contato específico')
    print('4 - Mostrar agenda')
    print('5 - Sair')
    print('-'*70)

    opcao = input('Escolha uma opção (1-5):')

    if opcao == '1':
        # Adicionar um contato
        nome = input('Digite o nome do contato.')
        telefone = input('Digite o telefone do contato: ')
        agenda[nome] = telefone
        print(f'Contato{nome}:{telefone} adicionado.')

    elif opcao == '2':
        # remover um contato
        nome = input('Digite o nome do contato que deseja remover: ')
        if nome in agenda:
            del agenda[nome]
            print(f'Contato {nome} removido.')
        else:
            print(f'Contato {nome} não encontrado na agenda.')

    elif opcao == '3':
        # verificar contato especifico
        nome = input('Digite o nome do contato que deseja verificar: ')
        if nome in agenda:
            print(f'Contato encontrado - {nome}: {agenda[nome]}')
        else:
            print(f'Contato {nome} não encontrado na agenda.')
    elif opcao == '4':
        # Mostrar agenda atual
        print('\nAgenda de Contatos:')
        print(agenda)
