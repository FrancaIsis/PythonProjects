import csv
import os


#nome do arquivo CSV
arquivo = 'arquivos_csv/gravacao/alunas.csv'

# lista para armazenar dados
lista = []

# abrindo o arquivo csv para leitura
with open(arquivo,'r') as arquivo_csv:
    # criando um leitor de CSV que lê o arquivo como dicionario
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    
    # Iterando sobre cada linha (registro) no arquivo CSV e adicionando à ista
    for linha in leitura:
        lista.append(linha)
        
os.system('cls')
print('-'*70)
print('nome\ttelefone\tcidade')
print('='*70)
# exibindo a lista resultante
for registro in lista:
    flag = 0
    for k, v in registro.items():
        print(v, end='\t')
        flag += 1
        if flag == 3:
            print()
print('-'*70)