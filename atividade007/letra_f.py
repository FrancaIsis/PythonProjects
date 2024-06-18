# Isis de Oliveira Silva França
# Turma 0152
# Atividade 007
# Faça um programa que gere 10 números aleatórios. Após gerar esses números,
# crie duas listas novas com ordenação ascendente e descendente.
import os
import random


os.system('cls')

print('-'*70)
print('ORDENAÇÃO ASC E DESC:')
print('='*70)

# inicializando variaveis
lista = []

for i in range(10):
    numero = random.randint(0, 100)
    lista.append(numero)

print(f'A lista gerada foi:\n{lista}\n')
lista.sort()
print(f'A lista ordenada de forma ascendente é: \n{lista}\n')
lista.sort(reverse=True)
print(f'A lista ordenada de forma descendente é: \n{lista}\n')
