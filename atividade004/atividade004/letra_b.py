# Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 'Silva' por 'Oliveira'.

# importando bibliotecas
import os


os.system('cls')

print('-' * 70)
print('SUBSTITUTOS')
print('=' * 70)

# inicializando variaveis

nome = 'João da Silva'

# substituindo

substituicao = nome.replace('Silva', 'Oliveira')

# saída de dados

print(f'O primeiro nome armazenado era: {nome}')
print(f'Após a substituição temos: {substituicao}')
print()