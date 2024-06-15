# Isis de Oliveira Silva França
# Turma 0152
# Atividade 006
# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os


os.system('cls')

print('-'*70)
print('CRIANDO E SOMANDO')
print('='*70)

# inicializando variaveis
lista = []
soma = 0
# criando a lista
while len(lista) < 5:
    valor = input('Digite um número inteiro: ')
    if valor.isdigit(): # retorna true se for uma string em "forma" de digito
        valor_inteiro = int(valor) # realiza um casting
        lista.append(valor_inteiro) # acrescenta o item à lista 
        soma += valor_inteiro
    else:
        print('Informe um valor válido.')

print(f'Os números digitados foram: {lista}')
print(f'A soma desses valores é: {soma}')

