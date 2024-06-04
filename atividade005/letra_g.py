# # Isis de Oliveira Silva França
# Turma 0152
# Atividade 005

# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.
# Um número é classificado como primo se ele é maior do que um e é divisível apenas por um e por ele mesmo.
# Apenas números naturais são classificados como primos.
import os
import math


os.system('cls')

print('-'*70)
print('NÚMEROS PRIMOS')
print('='*70)

# inicializando variaveis

numero_inicial = 0
numero_final = 0
contador = 0
lista = []

# entrada de dados

numero_inicial = int(input('Informe o primeiro número do intervalo: '))
numero_final = int(input('Informe o último número do intervalo: ')) + 1

# processamento

if numero_inicial < 2:  # nao tem numero primo menor do que 2
    numero_inicial = 2

# varrendo o intervalo e verificando se o número é divisível por outro alem dele
for i in range(numero_inicial, numero_final):
    for j in range(numero_inicial, i):
        if i % j == 0:
            break  # se houver uma divisao exata o loop é interrompido
    else:
        print(i)  # mostrando os numeros primos
