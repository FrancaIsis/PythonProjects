# Faça um programa que receba um valor e mostre sua raiz quadrada. Para raízes que não são exatas,
# arredonde para cima ou para baixo. Faça a validação para números negativos, avisando ao usuário
# que o resultado será um número complexo.

# importando as bibliotecas
import math
import cmath
import os


# limpando os dados do terminal
os.system('cls')

print('-'*70)
print('RAÍZES')
print('='*70)
print()

# inicializando as variáveis
numero = 0
raiz = 0

# entrada de dados
numero = int(input('Digite um número e descubra sua raiz quadrada: '))

# processamento
#validação número negativo
if numero > 0:
    raiz = math.sqrt(numero)
    if (raiz % 2) != 0:
        
        print(f'A raiz quadrada de {numero} arredondada para cima é {math.ceil(raiz)}. ')
        print(f'A raiz quadrada de {numero} arredondada para baixo é {math.floor(raiz)}. ')
        print()
    else:
        print(f'A raiz quadrada de {numero} é {raiz}. ')
 
 
else:
    raiz = cmath.sqrt(numero)
    print('Você informou um número negativo, portanto o resultado será um número complexo!')
    print(f'A raiz quadrada de {numero} é {raiz}')





