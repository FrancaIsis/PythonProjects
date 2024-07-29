# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Uma Academia deseja fazer uma pesquisa entre seus clientes
# para descobrir a média de altura e peso de seus clientes. 
# Faça um programa que pergunte a cada um dos clientes da academia 
# seu código, nome, altura e peso. Após esse cadastramento, 
# seu programa deverá listar os dados dos clientes e a média. 
# Para sair do programa o usuário deverá digitar o valor zero(0). 
# O número de clientes é indefinido. Veja a saída no próximo slide.

import os
import statistics


os.system('cls')

cadastro = {}
lista = []

print('-'*70)
print('ACADEMIA')
print('='*70)


def cadastrar_clientes():
    cadastro['matricula'] = input('Informe o número da matrícula: ')
    cadastro['nome'] = input('Digite o nome completo: ')
    cadastro['altura'] = float(input('Informe a altura: '))
    cadastro['peso'] = float(input('Informe o peso: '))
    # salvando os dados em uma lista
    lista.append(cadastro.copy())

def mostrar_clientes():
    somatorio_altura = 0
    somatorio_peso = 0
    for cadastro in lista:
        somatorio_altura += cadastro['altura']
        somatorio_peso += cadastro['peso']
        for chave, valor in cadastro.items():
            print(f'{chave} - {valor}')
        print('='*70)
    print()
    print('-'*70)
    media_altura = somatorio_altura/len(lista)
    media_peso = somatorio_peso/len(lista)
    print(f'A média de altura das pessoas cadastradas é: {media_altura:.2f}')
    print(f'A média de peso das pessoas cadastradas é: {media_peso:.2f}')
    print('-'*70)
def menu_cadastro():
    print('\nAcademia\n'
       '1. Cadastrar dados do cliente: \n'
       '2. Mostrar clientes cadastrados e média: \n'
       '3. Sair\n')

while True:
    menu_cadastro()
    opcao = int(input('Digite a opcao desejada: '))

    if opcao == 1:
        cadastrar_clientes()
    elif opcao == 2:
        mostrar_clientes()
    else:
        print('Saindo...')
        break
