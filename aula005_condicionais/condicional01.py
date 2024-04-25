# Curso de Deenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis França
# Data: 24/04/2024
# Estudo de Condicionais: Parte 1
# Objetivo: Verificando um valor decimal

import os# importando biblioteca responsável por interagir com o OS

os.system('cls') #limpando os dados do terminal

print('-'*70)
print('Estudo de condicional: Parte 1')
print('-'*70)

# Entrada
valor = float(input('Digite um número decimal: '))
resposta = ''

# Condicional
if valor % 2 == 0:
    resposta = f'Entrada incorreta, o valor {valor:.0f} é um inteiro!'
else:
    resposta = f'Entrada correta, o valor {valor} é um decimal!'
    
# Saída
print('-'*70)
print(resposta)

print('Fim do programa!\n')