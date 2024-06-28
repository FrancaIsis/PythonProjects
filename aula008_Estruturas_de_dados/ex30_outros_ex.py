import os


os.system('cls')

# Inicializando o dicionario e a lista
elementos = {} # dicionario
periodica = [] # Lista

# Entrada de dados
for c in range(2): # considerando a entrada de 2 elementos
    print(f'Entrada de dados {c + 1}:')
    simbolo = str(input('Símbolo do elemento: '))
    nome = str(input('Nome do elemento: '))
    
    # adiciona os dados ao dicionario
    elementos['Símbolo'] = simbolo  
    elementos['nome'] = nome
    
    # usa o append() oom copy() para adicionar uma cópia do dicionario à lista
    periodica.append(elementos.copy())
    
print()
print('-'*70)
print('Elementos na tabela periódica: ')
print(periodica)
print('-'*70)
print()

# For aninhado para percorrer a lista e o dicionario
print('Detalhes dos elementos: ')
for elemento in periodica: #para cada elemento na lista ou para cada dicionario na lista
    for chave, valor in elemento.items(): # para cada chave e valor do dicionario
        print(f'{chave.capitalize()}:{valor}')# imprime a chave e o valor de maneira legivel
    print('-'*70) # Linha separada entre os elementos
    
    