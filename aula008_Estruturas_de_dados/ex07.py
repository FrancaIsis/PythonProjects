import os


os.system('cls')

# Solicita ao usuario para inserir numeros separados por espaço
entrada = input('Digite números separados por espaço')

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# converte  a lista de strings  em uma lista de inteiros
numeros = []

for num_str in numeros_str:
    numeros.append(int(num_str))

# solicita ao usuario para inserir o numero que deseja contar na lista
numero_para_contar = int(input('Digite o numero que deseja contar: '))

# conta o numero de vezes que o número fornecido aparece na lista
contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f'O número {numero_para_contar} aparece {contagem} vezes na lista.')
else:
    print(f'O número {numero_para_contar} não aparece na lista.')

# exibe a lista fornecida para conferência
print(f'Lista fornecida: {numeros}')
