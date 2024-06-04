# Isis de Oliveira Silva França
# Turma 0152
# Atividade 005

# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares,
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo,
# assim como a soma dos mesmos.

import os


os.system('cls')

print('-'*70)
print('conta ímpares')
print('='*70)

# inicializando variaveis
soma = 0
contador = 0
inicio = 1
fim = 100

# looping

for i in range(inicio, fim + 1):
    if i % 2 != 0:
        contador += 1
        soma += i

# saída de dados
print(f'A contagem de números ímpares é: {contador}')
print(f'A soma dos números ímpares encontrados é: {soma}')
