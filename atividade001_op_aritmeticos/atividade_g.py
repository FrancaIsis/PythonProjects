# Faça um programa que converta metros em centímetros e milímetros.
# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.
# 1 metro tem 100 centrimetros e 1000 milimetros
# importando a biblioteca OS que faz a interação com o SO
import os


# limpando dados do terminal
os.system('cls')

# inicializando as variáveis
metro = 0.0
centimetro = 0.0
milimetro = 0.0

# entrada de dados
print('-'*70)
print('CONVERSÃO')
print('-'*70)

metro = float(input('Informe a metragem: '))

# processamento
centimetro = metro * 100
milimetro = metro * 1000

# saída de dados
print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'A metragem informada foi {metro}\n'
      f'Esse valor em centímetros é {centimetro}\n'
      f'Esse valor em milímetros é {milimetro}')
print('')
