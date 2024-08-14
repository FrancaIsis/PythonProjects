# importar a bilbioteca CSV
import csv
import os

# criando uma lista de dicionarios: cada dicionario é uma linha (registro)
lista = [
    {'nome': 'Agata', 'telefone': '(32)99552-5454', 'cidade': 'Juiz de Fora'},
    {'nome': 'Bia', 'telefone': '(32)99567-5787', 'cidade': 'Juiz de Fora'},
    {'nome': 'Coly', 'telefone': '(32)94488-2244', 'cidade': 'Juiz de Fora'},
    {'nome': 'Isis', 'telefone': '(32)95544-4499', 'cidade': 'Juiz de Fora'},
]

# caminho para a pasta onde o arquivo csv será salvo
pasta = 'arquivos_csv/gravacao/'

# verificando se a pasta existe, se não, irá criá-la
os.makedirs(pasta, exist_ok=True)

# nome para o arquivo csv para gravar as informações
arquivo = 'arquivos_csv/gravacao/alunas.csv'

# caminho completo do arquivo csv
caminho_arquivo = os.path.join(pasta, arquivo)

# abre o arquivo 'arquivo' no modo de escrita ('w').
# Se o arquivo não existir, ele será criado; se existir, será truncado (esvaziado).
# newline = '':Evita a adição de linhas em branco extras ao gravar o arquivo em algumas plataformas.
# as arquivo_csv: atribui o objeto arquivo ao 'arquivo_csv' para ser usado dentro do bloco with.
with open(arquivo, 'w', newline='') as arquivo_csv:
    # campos = ['nome','telefone','cidade']:Define a lista de nomes de campos
    # cabeçalhosdas colunas do csv
    campos = ['nome', 'telefone', 'cidade']

    # writer = csv.DictWriter(arquivo_csv, fieldnames = campos):
    # cria um objeto DictWriter que usará 'arquivo_csv' para gravar os campos.
    # fieldnames define a ordem dos campos no arquivo csv
    # delimiter = ';': é o separador

    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')

    # writer.writeheader(): Grava a linha de cabeçalho no
    # arquivo csv usando os nomes de campos definidos em fieldnames.
    escrever.writeheader()

    # writer.writerows(lista): grava todas as linhas da lista no arquivo csv
    # cada dicionario em 'lista' se torna uma linha no arquivo.
    escrever.writerows(lista)

os.system('cls')
# exibe uma mensagem indicando que o arquivo foi gravado com sucesso
print(f'Arquivo {arquivo} gravado com sucesso!')
