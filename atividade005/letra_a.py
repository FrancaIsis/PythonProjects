# Isis de Oliveira Silva França
# Turma 0152
# Atividade 005
# Faça um programa que imprima os números no intervalo entre 1 e 100. Os números devem ser apresentados na horizontal.
import os


os.system('cls')

print('-'*70)
print('IMPRIMINDO DE 0 A 100')
print('='*70)

# inicializando variaveis
inicio = 1
fim = 100

# processamento/ looping

for i in range(inicio, fim+1):  # o for tem intervalo fechado no começo e aberto do final
    print(i, end=' | ')
