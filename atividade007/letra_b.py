# Isis de Oliveira Silva França
# Turma 0152
# Atividade 007
# Faça um programa que preencha uma lista
# com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.
import os, random


os.system('cls')

print('-'*70)
print('50 NUMEROS:')
print('='*70)

# inicializando variaveis
lista = []

for i in range(50):
    numero = random.randint(0,100)
    lista.append(numero)

print(lista)
print()
#lista fatiada
lista_fatiada = lista[0:50:10]
print(lista_fatiada)