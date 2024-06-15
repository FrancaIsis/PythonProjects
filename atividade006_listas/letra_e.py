# Isis de Oliveira Silva França
# Turma 0152
# Atividade 006
# Faça um programa que leia as vogais, depois mostre-as em ordem inversa.

import os


os.system('cls')

print('-'*70)
print('VOGAIS:')
print('='*70)

# inicializando variaveis
vogais = []
vogais_estabelecidas = ['a','e','i','o','u']
vogais_invertidas = []
# entrada de dados
for i in range (5):    
    while True:
        vogal = input('Informe a vogal: ')
        if vogal in vogais_estabelecidas: # verifica se a string está relacionada entre as vogais.
            vogais.append(vogal)
            break # pra sair do loop do while
        else:
            print('Informe um valor válido')

print(f'Vogais que você digitou: {vogais}')
vogais.reverse() # usando metodo para inverter
print(f'Vogais na ordem inversa: {vogais}')