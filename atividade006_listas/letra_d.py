# Isis de Oliveira Silva França
# Turma 0152
# Atividade 006
# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

import os


os.system('cls')

print('-'*70)
print('CALCULANDO A MÉDIA:')
print('='*70)

# inicializando variaveis
notas = []
media = 0.0
soma = 0

# recebendo dados
while len(notas) < 4:
    n = input('Informe a nota (valor inteiro): ')
    #validação
    if n.isdigit():
        n = int(n)
        notas.append(n) # acrescenta o valor a lista
        soma += n
    else:
        print('Informe um numero válido.')

# calculo da media
media = soma/len(notas)

# saida de dados
print(f'A notas informadas foram: {notas} e a média é {media}')