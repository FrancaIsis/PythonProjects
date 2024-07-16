# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Crie uma função que receba uma lista de números. Depois retorne duas listas com os números pares,
# os números ímpares, a quantidade de números pares e a quantidade de números ímpares.

import os


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
    print(f'Você informou {len(par)} números pares, os quais são: {par}')
    print(f'Você informou {len(impar)} números ímpares, os quais são: {impar}')

#inserindo os numeros na lista
while len(lista)<10:
    numero = int(input('Informe um número: '))
    if numero not in lista:
        lista.append(numero)
        
  
# chamando a função e passando o argumento lista
transformar_listas(lista)


    