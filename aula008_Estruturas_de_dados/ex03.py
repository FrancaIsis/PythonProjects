import os


os.system('cls')

# inicializa uma lista vazia
lista_numeros = []

# pede ao usuario para inserir 3 numeros
for i in range(3):
    numero = int(input('Digite um número: '))
    
    # adiciona um numero à lista
    lista_numeros.append(numero)
                         
# verifica se o numero inserido está na lista e 
# #exibe uma mensagem correspondente
numero_verificar = int(input('Digite um numero: '))

if numero_verificar in lista_numeros:
    print(f'O numero {numero_verificar} está na lista!')
else:
    print(f'O numero {numero_verificar} não está na lista!')
