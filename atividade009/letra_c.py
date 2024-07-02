# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Utilizando o exercício anterior , retire um elemento do dicionário.
import os


os.system('cls')

dicionario = {}

print('-'*70)
print('Retirando elementos')
print('='*70)

for i in range(1, 5):
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    dicionario[chave] = valor
    print('-'*70)
    print(f'\n{i}° par {chave}:{valor} adicionado.')
    print('-'*70)


print(dicionario)

while True:

    adiciona = input('O que deseja fazer:'
                     '\n1 - Adicionar mais elementos'
                     '\n2 - Excluir um elemento'
                     '\n3 - Sair\n')

    if adiciona == '1':
        for i in range(1, 3):
            chave = input('Digite a chave: ')
            valor = input('Digite o valor: ')
            dicionario[chave] = valor
            print('-'*70)
            print(f'\n{i}° par {chave}:{valor} adicionado.')
            print('-'*70)

        print('Dicionário após a inclusão:')
        print(dicionario.items())
        print('-'*70)

    elif adiciona == '2':
        chave = input('Digite a chave (campo) que deseja excluir:')
        if chave in dicionario:
            del dicionario[chave]
            print(f'Registro {chave}:{valor} removido com sucesso:')
            print('-'*70)
        else:
            print('Campo não encontrado.')

    elif adiciona == '3':
        print('Fim do programa.')
        break
    else:
        print('Opção inválida. Tente novamente.')
