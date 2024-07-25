# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11. 
# Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 4. Divisão inteira : 
# 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6. 
# Em seguida, você criará funções que retornem os resultados das operações, 
# imprimindo os resultados na tela.
import os


os.system('cls')


print('-'*70)
print('OPERAÇÕES MATEMÁTICAS')
print('='*70)

print('Informe dois números entre 1 e 10:\n')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

def menu():
    print('\n1. Soma\n'
       '2. Subtração\n'
       '3. Produto\n'
       '4. Divisão\n'
       '5. Divisão inteira\n'
       '6. Resto da divisão\n'
       '0. Sair\n')
    print('=' * 70)

def soma(n1,n2):
    soma = n1 + n2
    return soma

def subtracao(n1,n2):
    subtracao = n1 - n2
    return subtracao

def produto(n1,n2):
    produto = n1 * n2
    return produto

def divisao(n1,n2):
    divisao = n1/n2
    return divisao

def divisao_inteira(n1,n2):
    divisao_inteira = n1//n2
    return divisao_inteira

def resto_divisao(n1,n2):
    resto_divisao = n1 % n2
    return resto_divisao

if n1 > 0 and n1 < 11 and n2 > 0 and n2 < 11:
    while True:
        menu()
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            resultado_soma = soma(n1,n2)
            print(f'O resultado da soma de {n1} e {n2} é = > {resultado_soma}')
        elif opcao == 2:
            resultado_subtracao = subtracao(n1,n2)
            print(f'O resultado da subtração de {n1} e {n2} é = > {resultado_subtracao}')
        elif opcao == 3:
            resultado_produto = produto(n1,n2)
            print(f'O resultado da multiplicação de {n1} e {n2} é = > {resultado_produto}')
        elif opcao == 4:
            resultado_divisao = divisao(n1,n2)
            print(f'O resultado da divisao de {n1} e {n2} é = > {resultado_divisao}')
        elif opcao == 5:
            resultado_divisao_inteira = divisao_inteira(n1,n2)
            print(f'O resultado da divisão inteira de {n1} e {n2} é = > {resultado_divisao_inteira}')
        elif opcao == 6:
            resultado_resto_divisao = resto_divisao(n1,n2)
            print(f'O resultado do resto da divisão de {n1} e {n2} é = > {resultado_resto_divisao}')
        else:
            print('Saindo...\n') 
            break   


else:
    print('Números inválidos:')
    print('Informe dois números entre 1 e 10:\n')
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))


