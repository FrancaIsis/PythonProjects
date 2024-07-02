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
continua = 1


# menu
while True:
    menu = input('Escolha uma opção:\n'
                 '1 - Cadastrar\n'
                 '2 - Consultar\n'
                 '3 - Editar\n'
                 '4 - Excluir\n'
                 '0 - SAIR\n')
    print('-'*70)
    # verifica se o usuario digitou um valor numerico
    if menu.isdigit():
        # casting
        menu = int(menu)
        if menu == 0:
              break

        elif menu == 1:
            while True:
                #validação
                #n = input('Nome: ').lower().strip()
                #if n.isalpha():
                #    nome.append(n)
                #else:
                #     print('Informe um texto para o campo Nome.')
                
                # end = input('Endereço: ').lower().strip()
                # if end.isalnum():
                #    endereco.append(end)
                #else:
                #     print('Informe um valor válido para o campo Endereço.') 
                
                # tel = input('Telefone: ').strip()
                #if tel.isalnum():               
                #    telefone.append(tel)
                #else:
                #     print('Informe um valor válido para o campo Telefone.')
                nome.append(input('Nome: ').lower().strip())
                endereco.append(input('Endereço: ').lower().strip())
                telefone.append(input('Telefone: ').strip())
                     
                continua = int(input('Digite 1 para continuar ou 0 para sair:' )) 
                if continua == 0:
                    break
        elif menu == 2:
            # for para percorrer o cadastro
            for i in range(0,len(nome)):
                #for j in range(0,len(endereco)):
                print('-'*70)                     
                print(f'{nome[i]}\n{endereco[i]}\n{telefone[i]}')
                print('-'*70)
           
        elif menu == 3:
                print('Digite o número do registro deseja editar:\n')
                for i, nomes in enumerate(nome, start=1):                 
                    print(f'{i} - {nomes}')
                    print('-'*70)
                while True:
                     # recupera o indice do nome no cadastro para ser editado
                     indice = int(input('Digite o número do registro deseja editar:\n'))-1
                     if 0 <= indice < len(nome):
                          nome[indice] = input('Nome: ').lower().strip()
                          endereco[indice] = input('Endeço: ').lower().strip()
                          telefone[indice] = input('Telefone: ').strip()
                          break
                
        elif menu == 4:
                print('Digite o número do registro deseja excluir:\n')
                for i, nomes in enumerate(nome, start=1):
                    print(f'{i} - {nomes}')
                    print('-'*70)
                while True:
                # recupera o indice do nome no cadastro para ser excluido
                    indice = int(input('Digite o número do registro deseja excluir:\n'))-1
                    print('-'*70)
                    if 0 <= indice < len(nome):
                         nome_removido = nome.pop(indice)
                         endereco_removido = endereco.pop(indice)
                         telefone_removido = telefone.pop(indice)
                         print(f' O cadasto de {nome_removido} foi removido')
                         break
                     
            
    else:
        print('Digite um valor válido.')