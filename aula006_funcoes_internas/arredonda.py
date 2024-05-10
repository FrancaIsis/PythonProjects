import math
import os


os.system('cls')

print('-'*50)
print('ESTUDO DA BIBLIOTECA MATH')
print('='*50)
print()

#entrada de dados
numero_decimal = float(input('Entre com um número decimal: '))

#processamento
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal)

#saída
print('-'*50)
print(f'O número {numero_decimal} arredondado para cima é: {arredondar_para_cima}')
print(f'O número {numero_decimal} arredondado para baixo é: {arredondar_para_baixo}')
print('-'*50)