# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Crie uma função que verifica se uma aluno(a) está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados. 
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

import os


os.system('cls')


def verificar_cadastro(matricula,lista):
    '''Função que verifica se um aluno já esta cadastrado e retorna os dados'''
    for cadastro in lista:
        if cadastro['matricula'] == matricula:
            print(f'Os dados do aluno são:{cadastro.values()}')