# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Crie uma função que receba a altura e o peso de uma pessoa. Depois retorne o seu IMC.

# IMC = peso/(altura x altura)

import os


os.system('cls')

print('-' * 70)
print('IMC')
print('=' * 70)

print('\nresultados menores que 16 — magreza grave;\n'
       'resultados entre 16 e 16,9 — magreza moderada;\n'
       'resultados entre 17 e 18,5 — magreza leve;\n'
       'resultados entre 18,6 e 24,9 — peso ideal;\n'
       'resultados entre 25 e 29,9 — sobrepeso;\n'
       'resultados entre 30 e 34,9 — obesidade grau I;\n'
       'resultados entre 35 e 39,9 — obesidade grau II ou severa;\n'
       'resultados maiores do que 40 — obesidade grau III ou mórbida.\n')
print('=' * 70)


def calcular_imc(altura, peso):
    '''função que recebe o peso e a altura de alguem e calcula seu IMC'''
    imc = peso/altura**2
    return imc

altura = float(input('Informe a altura: '))
peso = float(input('Informe o peso: '))
print('-'*70)

# calculando imc usando a função criada
imc_calculado = calcular_imc(altura, peso)

# exibindo o resultado
print(f'O IMC para altura {altura:.2f} e peso {peso:.2f} é {imc_calculado:.2f}')
print('-' * 70)