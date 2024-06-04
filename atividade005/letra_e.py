# Isis de Oliveira Silva França
# Turma 0152
# Atividade 005

# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.
import os


os.system('cls')

print('-'*70)
print('SOMA NÚMEROS PARES')
print('='*70)

# inicializando variaveis
inicio = 0
fim = 100
soma = 0

# processamento/ looping

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma += 1

print(soma)
