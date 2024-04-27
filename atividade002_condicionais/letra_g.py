# Curso de Desenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis
# Data: 25/04/2024
# Atividade 002: Condicionais

# G) Você está desenvolvendo um programa para determinar se três segmentos podem formar um triângulo.
# Para isso, o programa precisa receber as medidas dos três segmentos e compará-las entre si.
# A resposta resultante dessa comparação deve indicar se os segmentos fornecidos podem formar um triângulo ou não.

# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

# importando a biblioteca
import os


# limpando dados do terminal
os.system('cls')

# inicializando as variaveis
lado_a = 0
lado_b = 0
lado_c = 0

# entrada de dados
lado_a = int(input('Digite o valor do primeiro lado: '))
lado_b = int(input('Digite o valor do segundo lado: '))
lado_c = int(input('Digite o valor do terceiro lado: '))

# conversão de numeros negativos
if lado_a < 0:
    lado_a = lado_a * -1
elif lado_b < 0:
    lado_b = lado_b * -1
elif lado_c < 0:
    lado_c = lado_c * -1
    
# processamento de dados/ saída



if(lado_b - lado_c) < lado_a and lado_a < (lado_b + lado_c):
    print('ok')
    print()
    if(lado_a - lado_c) < lado_b and lado_b < (lado_a + lado_c):
        print('ok')
        print()
        if(lado_a - lado_b) < lado_c and lado_c < (lado_a + lado_b):
            print('ok')
            print()
        else:
            print('Não é um triângulo:')
            print()
    else:
        print('Não é um triângulo:')
        print()
else:
    print('Não é um triângulo:')
    print()
    
    
    #    print('É um triângulo')
    #    print()
    #else:
    #    print('Não é um triângulo:')
    #   print()