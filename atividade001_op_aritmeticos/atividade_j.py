# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
# O perímetro de uma figura plana é igual à soma do comprimento de todos os lados dela.
# importando a biblioteca responsavel por interagir com o SO
# Perímetro do retângulo = 2 x (base + altura)
import os


# limpando os dados do terminal
os.system('cls')

# inicializando as variaveis
base = 0
altura = 0
perimetro = 0

print('-'*70)
print('CÁLCULO DO PERÍMETRO DE UM RETÂNGULO')
print('-'*70)

# entrada de dados
base = int(input('Informe o valor da base: '))
altura = int(input('Informe o valor da altura: '))

# processamento
perimetro = 2 * (base + altura)

# saida de dados
print('-'*70)
print('RESULTADO')
print('-'*70)
print(
    f'O perímetro do retângulo de base {base} e altura {altura} é {perimetro} !')
print('')
