# Isis de Oliveira Silva França
# Turma 0152
# Atividade 007
# Faça um programa que preencha uma lista
# com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.
import os
import random


os.system('cls')

print('-'*70)
print('50 NUMEROS:')
print('='*70)

# inicializando variaveis
lista = []

for i in range(50):
    numero = random.randint(0, 100)
    lista.append(numero)

print(lista)
print()
# lista fatiada
j = 10
for i in range(0, len(lista), 10):  # estou percorrendo a lista toda, com um intervalo de 10
    # aqui estou passando pra lista_fatiada o intervalo de i a j, considerando que o j ja esta começando c/10
    lista_fatiada = lista[i:j]
    i += 10
    j += 10
    print(lista_fatiada)
