# Faça um programa que receba um número inteiro e mostre na tela:
# A quantidade de unidades, a quantidade de dezenas, a quantidade de centenas e a quantidade de milhares.

#importando bibliotecas

import os


os.system('cls')

print('-' * 70)
print('Unidades, centenas, dezenas e milhares')
print('=' * 70)

# inicializando variaveis

numero = 0
unidade = 0
dezena = 0
centena = 0
milhar = 0

# entrada de dados 

numero = input('Digite um número e lhe revelaremos seus segredos....: ')
print('')
if not numero.isdigit():
    print('Digite um número inteiro!')
    print('')

else:
    numero = int(numero)
    unidade = numero // 1 % 10
    dezena = numero // 10 % 10
    centena = numero // 100 % 10
    milhar = numero // 1000 % 10


    print(f'O numero digitado foi: {numero}')
    print('-'*70)
    print(f'Unidade: {unidade}')
    print('-'*70)
    print(f'Dezena: {dezena}')
    print('-'*70)
    print(f'Centena: {centena}')
    print('-'*70)
    print(f'Milhar: {milhar}')
    print('-'*70)









