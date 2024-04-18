#imports
import os

#limpar os dados do terminal
os.system('cls')

print('-'*100)
print('OPERADORES ARITIMÉTICOS')
print('-'*100)

#Entrada de Dados
print('---- SOMA')
print('-'*100)
parcela_1 = float(input('Entre com a 1° parcela: '))
parcela_2 = float(input('Entre com a 2° parcela: '))

print()
print('---- SUBTRAÇÃO')
print('-'*100)
minuendo = float(input('Entre com o minuendo: '))
subtraendo = float(input('Entre com o subtraendo: '))

print()
print('---- PRODUTO')
print('-'*100)
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador: '))

print()
print('---- DIVISÃO')
print('-'*100)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

print()
print('----RAIZ')
print('-'*100)
radicando = int(input('Entre com o radicando: '))
indice = int(input('Entre com o índice: '))


#Processamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz = radicando * (1/indice)

#Saída
print('-'*100)
print('RESULTADOS')
print('-'*100)
print(f'A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} * {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} / {divisor} é: {quociente}')
print(f'A raiz de {radicando} no índice {indice} é: {raiz}')


