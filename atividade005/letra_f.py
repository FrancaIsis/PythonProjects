# Isis de Oliveira Silva França
# Turma 0152
# Atividade 005

# Faça um programa que imprima os números primos entre 0 e 100.
import os


os.system('cls')

print('-'*70)
print('Números primos 0 a 100')
print('='*70)

# inicializando variaveis

inicio = 0
fim = 100

# processamento

if inicio < 2:
    inicio = 2 # nao existe numero primo menor do que 2
    
for i in range (inicio, fim):# percorre os dados do intervalo, itera sobre a sequencia de elementos gerados no intervalo estabelecido
    for j in range (inicio, i): # percorre da variavel inicio ate o numero atual do indice i - 1 | pega do inicio ate os numeros menores q ele
        if i % j == 0:
            break # se o i for divisivel por j deu ruim, não é primo, parar o loop
    
    else:
        print(i)
