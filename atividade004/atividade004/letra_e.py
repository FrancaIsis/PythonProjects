# Faça um programa que receba uma frase e, em seguida, mostre quantas vezes as vogais foram utilizadas.

# importando bibliotecas

import os


os.system('cls')

print('-'*70)
print('VOGAIS')
print('='*70)

# INICIALIZANDO VARIAVEIS
frase = ''
lista = ''
contador, contador_a, contador_e, contador_i, contador_o, contador_u = 0, 0, 0, 0, 0, 0

#entrada de dados

frase = input('Digite uma frase: ').lower().strip()

# tratamento dos dados


lista = list(frase)

print(lista)


contador_a = lista.count('a')
contador_e = lista.count('e')
contador_i = lista.count('i')
contador_o = lista.count('o')
contador_u = lista.count('u')
contador = contador_a + contador_e + contador_i + contador_o + contador_u

print(f'O numero de vezes em que a vogal "a" aparece é: {contador_a}')
print('-'*70)
print(f'O numero de vezes em que a vogal "e" aparece é: {contador_e}')
print('-'*70)
print(f'O numero de vezes em que a vogal "i" aparece é: {contador_i}')
print('-'*70)
print(f'O numero de vezes em que a vogal "o" aparece é: {contador_o}')
print('-'*70)
print(f'O numero de vezes em que a vogal "u" aparece é: {contador_u}')
print('-'*70)
print(f'O numero de vezes em que as vogais foram utilizadas foi: {contador}')
print('-'*70)