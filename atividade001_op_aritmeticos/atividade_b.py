# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

# realizando os imports
import os  # biblioteca para interagir com o SO
import datetime  # bliblioteca que retorna a data e hora do sistema

os.system('cls')  # limpando os dados do terminal

# inicializando variaveis
ano_nascimento = 0
idade = 0
ano_atual = 0

print('-'*70)
print('CÁLCULO DA IDADE')
print('-'*70)

# entrada de dados
ano_nascimento = int(input('Informe o ano do seu ano_nascimento: '))
ano_atual = datetime.datetime.now().year  # retorna string

# processamento
idade = int(ano_atual) - ano_nascimento

# saida de dados
print('-'*70)
print(
    f'Considerando que o ano do seu nascimento é {ano_nascimento}, sua idade atual é {idade} anos!!')
print('-'*70)
