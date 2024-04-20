# Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores.
# Efetuando os imports
import os
# limpando os dados do terminal
os.system('cls')

print('-'*70)
print('SOMA E MULTIPLICAÇÃO')
print('-'*70)

# inicializando variáveis
soma = 0
multiplicacao = 0

# entrada de dados
numero_1 = int(input('Informe o primeiro número: '))
numero_2 = int(input('Informe o segundo número: '))
numero_3 = int(input('Informe o terceiro número: '))

# processamento
soma = numero_1 + numero_2 + numero_3
multiplicacao = numero_1 * numero_2 * numero_3

# saida de dados
print('-'*70)
print('Resultados:')
print('-'*70)
print(f'A soma dos números {numero_1}, {numero_2} e {numero_3} é {soma}')
print('')
print(
    f'O produto dos números {numero_1}, {numero_2} e {numero_3} é {multiplicacao}')
print('')
