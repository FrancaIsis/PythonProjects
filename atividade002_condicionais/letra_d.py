# Curso de Desenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis
# Data: 25/04/2024
# Atividade 002: Condicionais

# D) A empresa "SalaryBoost" está implementando um sistema automatizado para calcular os aumentos salariais de seus funcionários
# com base em critérios específicos. Eles precisam de um programa que receba como entrada o salário atual de um funcionário e,
# em seguida, calcule o novo salário com base em determinadas condições. Essas condições incluem um aumento de 5% caso o salário
# atual seja superior a R$1500,00, e um aumento de 10% caso o salário atual seja inferior a R$1000,00. Além disso, o programa deve
# garantir que o salário informado não seja igual a zero ou negativo, pois isso não seria válido.

# importanto bibiotecas
import os


# limpando dados do terminal
os.system('cls')

print('-'*70)
print('AUMENTO SALARIAL')
print('='*70)

# Inicializando variáveis

salario_atual = 0.0
novo_salario = 0.0

# entrada de dados

salario_atual = float(input('Digite o salário do funcionário: '))

# processamento/ saída de dados

if salario_atual > 0.0:
    if (salario_atual > 1500.00):
        novo_salario = salario_atual * 1.05
        print(
            f'Parabéns, você tinha um salário de R$ {salario_atual} e recebeu um aumento de 5%. Seu novo salário é de R$ {novo_salario :.2f}!')
        print()

    elif (salario_atual < 1000.00):
        novo_salario = salario_atual * 1.10
        print(
            f'Parabéns, você tinha um salário de R$ {salario_atual} e recebeu um aumento de 10%. Seu novo salário é de R$ {novo_salario :.2f}!')
        print()

    elif (salario_atual >= 1000.00 and salario_atual <= 1500.00):
        print(
            f'Lamentamos, mas seu salário é de {salario_atual} e não está entre os valores contemplados com o aumento deste ano.')
        print()

else:
    print('Valor inválido. Digite um valor maior que zero!')

print('-'*70)
print('Fim do programa')
print('='*70)
