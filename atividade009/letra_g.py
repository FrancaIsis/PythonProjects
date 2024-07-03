# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Faça um programa para cadastrar os alunos de uma escola.
# Para os campos, tome como referência o nome do aluno, data de nascimento e matrícula.
import os


os.system('cls')

print('-' * 70)
print('CADASTRO DE ALUNOS')
print('=' * 70)

cadastro = {}
lista = []
opcao = ''
contador = 0

while opcao != 's':
    cadastro['Nome'] = input('Nome: ')
    cadastro['Data_Nascimento'] = input('Data de nascimento:(dd/mm/aaaa) ')
    cadastro['Matricula'] = input('Matrícula: ')
    lista.append(cadastro.copy())
    opcao = input('Deseja sair? (s/n)').lower().strip()

print('='*70)

for elemento in lista:
    for chave, valor in elemento.items():
        print(f'{chave}:{valor}', end='\n')
    print('='*70)

