# Isis de Oliveira Silva França
# Turma 0152
# Atividade 007
# Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.
import os


os.system('cls')

print('-'*70)
print('LISTA NOMES:')
print('='*70)

# inicializando variaveis
lista = []
#contador = 0

for i in range(5):
    while True:
        nome = input('Digite um nome: ').lower().strip().capitalize()
        if nome.isalpha():
            lista.append(nome)
            break
        else:
            print('Informe um valor válido.')

if 'Pedro' in lista:
    print()
    print('Isso aí, Pedro está na lista!')

else:
    print()
    print('Xi! Pedro não está na lista')

print()
print(lista)
