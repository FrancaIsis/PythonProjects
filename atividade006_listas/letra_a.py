# Isis de Oliveira Silva França
# Turma 0152
# Atividade 006
# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

import os


os.system('cls')

print('-'*70)
print('INSERINDO O NÚMERO FALTANTE')
print('='*70)

# criando a lista
lista = [1, 2, 3, 5, 6]

print(lista)

while True:
# solicitando ao usuario que informe o valor que está faltando
    valor_faltante = input('Informe o valor que está faltando na lista acima: ')
    posicao = input('Informe a posição em que esse valor deverá ser inserido: ')

    if valor_faltante.isdigit() and posicao.isdigit():
        valor_faltante = int(valor_faltante)# realiza um casting
        posicao = int(posicao)-1 # realiza casting
            
        lista.insert(posicao, valor_faltante)

        # saida de dados
        print(f'Sua nova lista é: {lista}')
        break
    else:
        print('Informe um valor válido.')
