# Curso de Desenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis
# Data: 25/04/2024
# Atividade 002: Condicionais

# LETRA A - A empresa "TechSolutions" contratou você para desenvolver um programa em Python que
# irá automatizar uma parte do seu sistema de processamento de dados.
# Eles precisam de um programa que solicite ao usuário a entrada de um número inteiro e,
# em seguida, verifique se esse número é par ou ímpar.
# Essa funcionalidade é essencial para o sistema deles, pois eles processam grandes conjuntos de dados e
# precisam classificar os números de forma eficiente para realizar cálculos específicos em cada tipo de número.

# importando as bibliotecas
import os


# limpando os dados do terminal
os.system('cls')

print('-'*70)
print('PAR OU ÍMPAR')
print('='*70)

# inicializando as variaveis
numero = 0

# entrada de dados
numero = int(input('Digite um numero inteiro: '))
print('')

# processamento de dados e saída de dados
if numero % 2 == 0:
    print(f'O número {numero} é par!!')
else:
    print(f'O número {numero} é ímpar.')






