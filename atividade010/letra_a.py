# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Crie uma função que receba uma lista de números. Depois retorne duas listas com os números pares,
# os números ímpares, a quantidade de números pares e a quantidade de números ímpares.

import os
import random


os.system('cls')

par = []
impar = []
lista = []


def transformar_listas(lista):
    '''Função que recebe uma lista e calcula os numeros pares e impares'''
    for i in lista:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    quantidade_par = len(par)
    quantidade_impar = len(impar)
    return par, impar, quantidade_par, quantidade_impar  # empacotamento

    # print(f'Você informou {len(par)} números pares, os quais são: {par}')
    # print(f'Você informou {len(impar)} números ímpares, os quais são: {impar}')


# inserindo os numeros na lista com list comprehension
lista = list(random.randint(1, 100) for i in range(10))


# chamando a função e passando o argumento lista
par, impar, qtde_par, qtde_impar = transformar_listas(lista)

print(f'A lista de números gerada foi {lista}\n'
      f'Pares = {par}\n'
      f'Impares = {impar}\n'
      f'Quantidade de numeros pares = {qtde_par}\n'
      f'Quantidade de numeros ímpares = {qtde_impar}\n')
