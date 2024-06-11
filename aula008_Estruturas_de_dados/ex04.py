import os


os.system('cls')

# inicializa lista vazia
lista_numeros = []

# solicita ao usuario que insira numeros separados por espaço
entrada = input('Digite números separados por espaço: ')

# divide a string de entrada em uma lista de strings
numeros = entrada.split()

# cria uma lista para armazenar os numeros pares
pares = []

# itera sobre os numeros inseridos
for numero in numeros:
    # converte a string para inteiro
    numero_aux = int(numero)
    # verifica se o numero é par
    if numero_aux % 2 == 0:
        # adiciona o numero par à lista de pares
        pares.append(numero_aux)

# usa extend() para adicionar todos os numeros pares à lista principal
lista_numeros.extend(pares)

# exibe a lista resultante
print(f'Numeros pares adicionados à lista: {lista_numeros}')
