# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Crie uma função que cadastre o nome de um aluno(a), a matrícula e a data de nascimento. 
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.

import os
from letra_c import verificar_cadastro


os.system('cls')
cadastro = {}
lista = []

def cadastrar():
    cadastro['nome'] = input('Digite o nome:')
    cadastro['matricula'] = input('Digite a matricula: ')
    cadastro['Data_Nascimento'] = input('Informe a data de nascimento:')
    lista.append(cadastro.copy())
    
def imprimir_cadastro(lista):
    for cadastro in lista:
        for chave, valor in cadastro.items():
            print(f'{chave} - {valor}')
        print('-'*70)

# def verificar_cadastro(matricula):
#     '''Função que verifica se um aluno já esta cadastrado e retorna os dados'''
#     for cadastro in lista:
#         if cadastro['matricula'] == matricula:
#             print('ALUNO ENCONTRADO ok')


while True:
    print('-'*70)
    print('\nMenu de opções:')
    print('1 - Realizar cadastro')
    print('2 - Mostrar dados cadastrados')
    print('3 - Verificar Cadastro')
    print('4 - Sair')
    print('-'*70)

    opcao = input('O que você deseja fazer?\n')

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        imprimir_cadastro(lista)

    elif opcao == '3':
        matricula = input('Informe o numero da matricula que deseja buscar: ')
        verificar_cadastro(matricula,lista)

    elif opcao == '4':
        print('Encerrando...')
        break
    else:
        print('Opção invalida.')