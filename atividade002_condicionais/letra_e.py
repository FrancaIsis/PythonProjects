# Curso de Desenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis
# Data: 25/04/2024
# Atividade 002: Condicionais

# E) A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de preços de passagens de ônibus com base na distância da viagem.
# Eles precisam de um programa que solicite ao usuário a distância a desejada e, em seguida, calcule o preço da passagem de acordo com
# as políticas da empresa. Segundo essas políticas, viagens de até 200 km têm um custo de R$0,70 por km rodado, enquanto viagens acima
# dessa distância passam a custar R$0,40 por km rodado.

# importando as bibliotecas
import os


# limpando os dados do terminal
os.system('cls')

print('-'*70)
print('CÁLCULO DE PASSAGENS')
print('='*70)

# Inicializando variáveis
distancia = 0
passagem = 0.0

# entrada de dados
distancia = int(input('Informe a distância a ser percorrida: '))
print()

# processamento/ saída de dados
if distancia > 0:
    if distancia < 200:
        passagem = distancia * 0.70
        print(
            f'A distância a ser percorrida na sua viagem é de {distancia} km, portanto o valor da sua passagem será de R$ {passagem}.')
        print()
    elif distancia >= 200:
        passagem = distancia * 0.40
        print(
            f'A distância a ser percorrida na sua viagem é de {distancia} km, portanto o valor da sua passagem será de R$ {passagem}.')
        print()

else:
    print('Valor inválido')

print('-'*70)
print('Fim do programa')
print('='*70)
