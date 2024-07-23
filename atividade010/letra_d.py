# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.
# Subtraímos a temperatura em ºF por 32 e dividimos o resultado por 1,8
import os


os.system('cls')

def mudar_temperatura(temp_fahrennheit):
    temp_celsius = (temp_fahrennheit - 32)/1.8
    return temp_celsius

print('-' * 70)
print('CONVERSÃO DE TEMPERATURA')
print('=' * 70)

temp_fahrennheit = float(input('Informe a temperatura: '))
print(f'A temperatura {temp_fahrennheit} em Célsius é {mudar_temperatura(temp_fahrennheit):.2f}')
