# Curso de Desenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis
# Data: 25/04/2024
# Atividade 002: Condicionais

# H) A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes de equações quadráticas
# para auxiliar engenheiros e cientistas em suas análises e projetos. Eles precisam de um programa que
# calcule as raízes da equação quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos,
# utilizando apenas os conceitos e operações básicas aprendidos até o momento. Essas raízes são conhecidas
# como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser capaz de calcular essas raízes de forma precisa, seguindo
# os princípios matemáticos fundamentais.

#(-b±√(b²-4ac))/(2a)
#𝑥²−6𝑥+5

#importando as bibliotecas
import os


#limpando os dados do terminal
os.system('cls')

print('-'*70)
print('RAÍZES')
print('-'*70)
print('ax²+bx+c')
print('-'*70)
print('𝑥²−6𝑥+5')
print('='*70)

# inicializando as variaveis
a = 0
b = 0
c = 0
x1 = 0
x2 = 0
delta = 0

# entrada de dados
a = int(input('Informe o valor de a: '))
if a != 0:
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))
else:
    print('O valor de a não pode ser igual a zero!')
# processamento de dados

delta = (b**2)-(4*a*c)

x1 = (- b + (delta) ** 0.5)/ 2*a
x2 = (- b - (delta) ** 0.5)/ 2*a

# saida de dados
print('='*70)
print(f'A raízes da expressão 𝑥²−6𝑥+5 são:\n '
      f'x\' = {x1:.0f} e x" = {x2:.0f}')


