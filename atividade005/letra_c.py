# Isis de Oliveira Silva França
# Turma 0152
# Atividade 005
# Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.
import os


os.system('cls')

print('-'*70)
print('IMPRESSÃO INVERSA')
print('='*70)

# inicializando variaveis
inicio = 0
fim = 10
lista = []

# processamento/ looping

for i in range(inicio, fim + 1):
    lista += [i]
    
for i in reversed (lista):
    print(i, end= ' | ')
    
