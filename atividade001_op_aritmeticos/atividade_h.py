# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.
# importando a biblioteca OS que faz a interação com o SO
import os


os.system('cls')  # limpando os dados do terminal

# inicializando variaveis
numero = 0
multiplicacao = 0
i = 0

# entrada de dados
print('-'*70)
print('TABUADA')
print('-'*70)
numero = int(input('Informe o número: '))

# processamentoo de dados e saida de dados

print('-'*70)
while i < 10:
    multiplicacao = numero * i
    print(f'{numero} x {i} = {multiplicacao}')
    i = i+1

print('')
