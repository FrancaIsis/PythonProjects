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

# exibe a lista fornecida para referencia
print('Lista fornecida', numeros)

# Solicita ao usuario para decidir se deseja inverter a lista
escolha = input('Deseja inverter a ordem da lista? (s/n): ').strip().lower()

# verifica a escolha do usuario e inverte a lista se a resposta for 's'
if escolha == 's':
    numeros.reverse()
    print('Lista invertida:', numeros)
else:
    print('A lista não foi invertida.')
