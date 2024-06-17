# Isis de Oliveira Silva França
# Turma 0152
# Atividade 007
# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair).

# importando biblioteca
import os


# limpando dados
os.system('cls')

print('-'*70)
print('NOTAS')
print('='*70)

# inicializando variaveis

notas = []
#n = ''

while True:
    n = input('Informe a nota. Digite s ou 0 para SAIR: ').lower().strip()
    if n == 's' or n == '0':
        break

    else:
        if n.isdigit():
            n = int(n)
            notas.append(n)
        else:
            print('Informe um valor válido.')







