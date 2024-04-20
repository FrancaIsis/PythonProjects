# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.
# importando a biblioteca responsável por interagir com o SO
import os


# limpando os dados do terminal
os.system('cls')

# inicializando as variaveis
numero = 0
antecessor = 0
sucessor = 0

# entrada de dados
print('-'*70)
print('CÁLCULO DO ANTECESSOR E SUCESSOR')
print('-'*70)

numero = int(input('Digite um número: '))

# processamento de dados
antecessor = numero - 1
sucessor = numero + 1

# saida de dados
print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'O número digitado por você foi: {numero} \n'
      f'Seu antecessor é {antecessor}\n'
      f'Seu sucessor é {sucessor}\n')
print('')
