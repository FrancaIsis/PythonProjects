# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas
# realizando os imports
import os  # biblioteca para interagir com o SO

os.system('cls')  # limpando os dados do terminal

# inicializando as variaveis
nota_1 = 0.0
nota_2 = 0.0
nota_3 = 0.0
nota_4 = 0.0
media = 0.0
n = 4
soma = 0


print('-'*70)
print('CÁLCULO DA MÉDIA DE NOTAS')
print('-'*70)

# entrada de dados
nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))
nota_3 = float(input('Informe a terceira nota: '))
nota_4 = float(input('Informe a quarta nota: '))

# processamento de dados
soma = nota_1 + nota_2 + nota_3 + nota_4
media = soma / n

# saída de dados
print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'A média das notas informadas: \n '
      f'Primeira nota - {nota_1} \n'
      f'Segunda nota - {nota_2} \n'
      f'Terceira nota - {nota_3} \n'
      f'Quarta nota - {nota_4} \n\n'
      f'Média = {media}')
