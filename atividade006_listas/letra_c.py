# Isis de Oliveira Silva França
# Turma 0152
# Atividade 006

# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa
# • O produto dos intervalos 5-6 por 11-12

import os


os.system('cls')

print('-'*70)
print('TRABALHANDO COM NÚMEROS:')
print('='*70)

# inicializando variaveis
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
multiplos = []
produto = []
intervalo_1 = numeros[4:6]
intervalo_2 = numeros[10:12]

# for para calcular os multiplos
for i in numeros:
    if i % 2 == 0 or i % 3 == 0 or i % 4 == 0:
        multiplos.append(i)

# calculando o produto dos intervalos

for i in (intervalo_1):
    for j in (intervalo_2):
        produto.append(i * j)


# processamento e saida de dados
print(f'Nossa lista de números é composta por:\n {numeros}')
print('-'*70)
print(f'O intervalor de 1 a 9 é: \n {numeros[0:9]}')
print('-'*70)
print(f'O intervalor de 8 a 13 é: \n {numeros[7:13]}')
print('-'*70)
print(f'O números pares são: \n {[i for i in numeros if i % 2 == 0]}') # pares com list comprehensions
print('-'*70)
print(f'O números ímpares são: \n {[i for i in numeros if i % 2 != 0]}') # ímpares com list comprehensions
print('-'*70)
print(f'O números múltiplos de 2, 3 e 4 são: \n {multiplos}') 
print('-'*70)
print(f'Múltiplos de 2: \n {[i for i in numeros if i % 2 == 0]}') 
print('-'*70)
print(f'Múltiplos de 3: \n {[i for i in numeros if i % 3 == 0]}') 
print('-'*70)
print(f'Múltiplos de 4: \n {[i for i in numeros if i % 4 == 0]}') 
print('-'*70)
print(f'Lista reversa: {numeros[::-1]}')
print('-'*70)
print(f'O produto dos intervalos 5-6 por 11-12: {produto}')