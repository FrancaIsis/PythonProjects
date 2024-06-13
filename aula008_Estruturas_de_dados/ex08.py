import os


os.system('cls')

# solicita ao usuario para inserir numeros separados por espaço
entrada = input('Digite números separados por espaço: ')

# divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# converte a lista de strings em uma lista de inteiros
numeros = []

for num_str in numeros_str:
    numeros.append(int(num_str))

# solicita ao usuario para inserir o numero que deseja encontrar na lista
busca_numero = int(input('Digite o número que deseja encontrar: '))

# tenta encontrar o indice do numero fornecido
if busca_numero in numeros:
    indice = numeros.index(busca_numero)
    print(f'O número {busca_numero} está no índice {indice}.')
else:
    print(f'O número {busca_numero} não foi encontrado na lista.')

# Exibe a lista fornecida para conferência
print(f'Lista fornecida: {numeros}')
