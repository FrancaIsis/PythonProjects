# Isis de Oliveira Silva França
# Turma 0152
# Atividade 006
# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices

import os


os.system('cls')

print('-'*70)
print('ÍNDICES:')
print('='*70)

# inicializando variaveis
nomes = []

# entrada de dados com FOR
for i in range(5):
    while True:
        nome = input('Digite um nome: ')
        if nome.isalpha(): # verifica se a string é um caracter alfanumerico
            nomes.append(nome)
            break #sair do loop
        else:
            print('Informe um valor válido:')
# saída de dados com for..enumerate() - muito legal, usa tipo 2 parametros
for i, nome in enumerate(nomes):
    print(f'{i+1} - {nome}')

