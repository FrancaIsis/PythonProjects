# Isis de Oliveira Silva França
# Turma 0152
# Atividade 005
# Crie um programa que pede que o usuário digite um nome ou uma frase,
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

import os


os.system('cls')

print('-'*70)
print('PALÍNDROMO')
print('='*70)
print('')

#Inicializando variaveis

texto = ''

# entrada de dados
texto = input('Digite um nome ou frase e verifique se é ou não um palíndromo: ').lower().strip()
texto_inverso = texto[::-1]

print('')
print(texto,'\n')
print(texto_inverso, '\n')

if texto in texto_inverso:
    print('É um palíndromo \n')
else:
    print('Não é um palíndromo')
