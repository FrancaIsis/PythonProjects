import os


os.system('cls')

print('-'*70)
print('Saída com FOR')
print('='*70)

# criando uma lista
lista_alunos = []

for c in range(0, 5):
    nome = str(input('Entre com o nome do aluno: '))

    # Guardando em uma lista
    lista_alunos.append(nome)

print()
print('Impressão dos nomes de alunos: ')

# utilizando o len() para saber a quantidade de alunos
for aluno in range(len(lista_alunos)):
    print(lista_alunos[aluno], end='')
    if c == 3:
        print()

print()
print('-'*70)
print('Fim do programa!')
print('-'*70)
