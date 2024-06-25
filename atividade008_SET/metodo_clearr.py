# Trabalho sobre a estrutura de dados SET
# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Programa que exclui 

import os
import random


os.system('cls')


# Determnando o numero de elementos no SET
numero_itens = int(input('Você deseja um set com quanto elementos? '))

# sorteando numeros exclusivos de acordo com a quantidade estabelecida pelo usuario
elementos = random.sample(range(0, 100), numero_itens)

# criando um set
meu_set = set(elementos)
print('-'*70)
print(f'Meu SET: {meu_set}')
print('='*70)

# usando o metodo clear()
opcao = input('Deseja excluir os dados inseridos? (s/n)').lower().strip()

if opcao == 's':
    meu_set.clear()

print('-'*70)
print(f'Meu SET: {meu_set}')
print('-'*70)
