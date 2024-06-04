# Isis de Oliveira Silva França
# Turma 0152
# Atividade 005

# Faça um programa que imprima os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os


os.system('cls')

print('-'*70)
print('IGNORANDO NUMEROS')
print('='*70)

# inicializando variaveis

numero_inicio = 0
numero_final = 0
ignorado_1 = 3
ignorado_2 = 5
ignorado_3 = 7

# entrada de dados

numero_inicio = int(input('Informe o primeiro número do intervalo: '))
numero_final = int(input('Informe o último número do intervalo: ')) + 1

# processamento

for i in range(numero_inicio, numero_final):
    if i == ignorado_1 or i == ignorado_2 or i == ignorado_3:
        continue
    print(f'Número {i}')

print('-'*70)
print()
