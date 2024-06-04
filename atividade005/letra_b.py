# Isis de Oliveira Silva França
# Turma 0152
# Atividade 005
# Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver impresso.
import os


os.system('cls')

print('-'*70)
print('IMPRIMINDO INTERVALO ESCOLHIDO PELO USUARIO')
print('='*70)

# inicializando variaveis
inicio = int(input('Informe o primeiro número do intervalo: '))
fim = int(input('Informe o último número do intervalo: '))

# processamento/ looping

for i in range(inicio, fim + 1):
    print(i, end=' | ')
