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

# solicita ao usuario para decidir se deseja limpar a lista
escolha = input('Deseja criar uma cópia? (s/n): ').strip().lower()

# verifica a escolha de usuario e limpa a lista se a resposta for 's':
if escolha == 's':
    numeros.clear()
    print(f'Lista limpa: {numeros}')
else:
    print('A lista não foi limpa.')

# exibe a lista fornecida para referencia
print(f'Lista fornecida: {numeros}')
