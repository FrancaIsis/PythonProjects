# Desafio: Construa um código para exemplificar um CRUD. Não é permitido funções ou validações try exception.
# Create (criar), Read (ler), Update (atualizar) e Delete (apagar)

import os


os.system('cls')

print('-'*70)
print('DESAFIO - CRUD')
print('='*70)
print('Cadastro de pessoas')
print('-')
# Inicialização de variaveis

nome = []
endereco = []
telefone = []


# menu
while True:
    menu = input('Escolha uma opção:\n'
                 '1 - Cadastrar\n'
                 '2 - Consultar\n'
                 '3 - Editar\n'
                 '4 - Excluir\n'
                 '0 - SAIR')
    # verifica se o usuario digitor um valor numerico
    if menu.isdigit():
        # casting
        menu = int(menu)
        while menu != 0:
            pass
