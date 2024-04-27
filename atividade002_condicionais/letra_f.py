# Curso de Desenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis
# Data: 25/04/2024
# Atividade 002: Condicionais

# F) A empresa "LeapYearCheck" está desenvolvendo um software de verificação de anos bissextos para auxiliar usuários na identificação
# desses anos de forma rápida e precisa. Eles precisam de um programa que permita aos usuários inserir um ano e, em seguida, determine
# se esse ano é bissexto ou não, de acordo com as regras estabelecidas pelo calendário gregoriano. Além disso, é necessário realizar a
# validação de entrada de dados para garantir que o ano inserido pelo usuário seja um valor válido, ou seja, um número inteiro positivo.

# Para ser bissexto, o ano deve ser:
# Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
# Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
# Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.

# importando bibliotecas
import os


# limpando dados do terminal
os.system('cls')

print('-'*70)
print('ANO BISSEXTO')
print('='*70)

# inicializando as variáveis
ano = 0

# entrada de dados
ano = int(input('Informe o ano desejado: '))

# processamento/ saída de dados
if ano > 0:
    if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
        print(f'O ano {ano} é bissexto!')
        print()
    else:
        print(f'O ano {ano} não é bissexto!')
        print()
else:
    print('Valor inválido')

print('-'*70)
print('Fim do programa')
print('='*70)
