#imports
#Biblioteca para interagir a SO
import os
#Biblioteca para pegar data e hora do sistema
import datetime


#limpar o terminal
os.system('cls')

print('-'*70)
print('ENTRADA DE DADOS EM PYTHON')
print('-'*70)

#Entrada
nome = input('Entre com um nome: ')
peso = input('Entre com o peso: ')
altura = input('Entre com a altura: ')

#Entrada com Casting
nascimento = int(input('Ano de nascimento: '))
cep = int(input('Entre com o seu CEP: '))
bairro = str(input('Entre com o bairro: '))
rua = str(input('Nome da rua: '))
numero = int(input('Entre com o numero: '))

#Processamento: pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

#Saída
print('-'*70)
print('SAÍDA DE DADOS')
print('-'*70)
print('Nome -------------: ', nome)
print('Data de nascimento: ', nascimento)
print('Peso--------------: ', peso)
print('Altura -----------: ', altura)

#Saída interpolada
print(f'{nome}, você tem {idade} anos!')
print(f'CEP --------------: {cep}')
print(f'Bairro -----------: {bairro}')
print(f'Rua -----------: {rua}')
print(f'Número -----------: {numero}')
print('-'*70)
print('')