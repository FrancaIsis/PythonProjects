# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.
# importando a biblioteca responsável pela interação com o SO
import os


os.system('cls')  # limpando os dados do terminal

# inicializando as variaveis
numero_1 = 0
numero_2 = 0
divisao = 0.0

print('-'*70)
print('CÁLCULO DA DIVISÃO')
print('-'*70)

# entrada de dados
numero_1 = float(input('Informe o primeiro número: '))
numero_2 = float(input('Informe o segundo número (maior do que zero): '))

# processamento
divisao = numero_1/numero_2


# saida de dados
print('-'*70)
print('RESULTADO')
print('-'*70)
print(
    f'O resultado da divisão de {numero_1} pelo {numero_2} é {divisao:.4f} !')
print('')
