# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Utilizando o exercício anterior,  adicione mais 2 elementos ao dicionário.
import os


os.system('cls')

dicionario = {}

print('-'*70)
print('Adicionando mais elementos')
print('='*70)

for i in range(1, 5):
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    dicionario[chave] = valor
    print('-'*70)
    print(f'\n{i}° par {chave}:{valor} adicionado.')
    print('-'*70)


print(dicionario)

adiciona = input(
    'Deseja inserir mais dados ao dicionario?(s/n)').lower().strip()

if adiciona == 's':
    for i in range(1, 3):
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        dicionario[chave] = valor
        print('-'*70)
        print(f'\n{i}° par {chave}:{valor} adicionado.')
        print('-'*70)

    print('Dicionário após a inclusão:')
    print(dicionario)
else:
    print('Fim do programa.')
