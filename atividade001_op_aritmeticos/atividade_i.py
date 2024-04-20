# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.
# importando a biblioteca OS que faz a interação com o SO
import os


os.system('cls')  # limpando os dados do terminal

# inicializando variaveis
valor_reais = 0
dolar_cotacao = 0
dolar_compra = 0

# entrada de dados
print('-'*70)
print('CONVERSÃO DOLÁRES')
print('-'*70)
valor_reais = float(input('Informe o valor que você possui em reais: '))
dolar_cotacao = float(input('Informe a cotação do dolar hoje: '))

# processamento de dados
dolar_compra = valor_reais/dolar_cotacao

# saída de dados
print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'No momento você pode comprar {dolar_compra} doláres. Parabéns!')
print('')
