# Curso de Desenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis
# Data: 25/04/2024
# Estudo de Condicionais: Parte 4
# Operadores lógicos

# importando as bibliotecas
import os


# limpando o terminal
os.system('cls')

#Inicializando as variáveis
a = 10
b = 5
c = 'John'

print('-'*70)
print('Condicionais: Operadores lógicos')
print('='*70)

#E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: bloco executado')
    
print('-'*70)

#E (and) FALSO
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('-'*70)

# OU (or) VERDADEIRO
print('OU (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('-'*70)

#OU (or) FALSO
print('OU (or) FALSO')
if (a < 5 or c == 'Jane'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('-'*70)
print()