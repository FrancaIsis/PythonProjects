# imports
# Biblioteca para interagir a SO
import os
# Biblioteca para pegar data e hora do sistema
import datetime


# limpar o terminal
os.system('cls')

print('-'*70)
print('MATRÍCULA')
print('-'*70)

# inicializando a variavel
aluno_cadastrado = True

# Entrada
nome = input(str('Informe o nome do aluno: '))
cpf = int(input('CPF (apenas números): '))
matricula = int(input('Digite o numero da matrícula: '))
curso = str(input('Informe o curso: '))
cidade = str(input('Digite o nome da sua cidade: '))
valor_matricula = float(input('Informe o valor da matrícula: '))

# firula

print('-'*70)
print('CONFIRMAÇÃO DE MATRÍCULA')
print('-'*70)

# saída de dados com casting

mensagem = f'Bem vindo ao nosso curso {nome}! A turma de {curso} \n'\
    f'está muito feliz com a sua presença. \n\n'\
    f'Confira seus dados: \n\n'\
    f'{nome} possui o CPF: {cpf} e n° de matrícula {matricula}. \n'\
    f'É oriundo da cidade {cidade} e esta matriculado no curso de {curso}. \n'\
    f'O valor pago no ato da sua matrícula foi de R$ {valor_matricula}'

print(mensagem)

#informando o tipo das variaveis
print('')
print('A variável aluno_cadastrado é do tipo: ', type(aluno_cadastrado))
print('A variável nome é do tipo: ', type(nome))
print('A variável cpf é do tipo: ', type(cpf))
print('A variável matricula é do tipo: ', type(matricula))
print('A variável curso é do tipo: ', type(curso))
print('A variável valor_matricula é do tipo: ', type(valor_matricula))
