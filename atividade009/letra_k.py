# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Faça um programa que peça continuamente o nome e a idade de uma pessoa. 
# Caso o usuário digite a idade 999, o programa será finalizado e executará uma impressão com os nomes cadastrados.


import os


os.system('cls')

print('-' * 70)
print('NOMES')
print('=' * 70)

cadastro = {}


while True:
    nome = input('Digite o nome:')
    idade = int(input('Digite a idade: '))
    
    if nome not in cadastro:
        if idade != 999:
            cadastro[nome] = idade
        else:
            break
    else:
        print(f'O nome {nome} já está cadastrado.')
        
print(cadastro)