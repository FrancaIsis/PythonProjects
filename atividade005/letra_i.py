# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação.
# Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os


os.system('cls')

print('-'*70)
print('ADVINHA')
print('='*70)

# inicializando variaveis

letra_usuario = ''

# processamento
while letra_usuario != 'f':
    print('Estou em looping')
    print()
    letra_usuario = input('Digite uma letra para sair do looping: ').lower()

print('-'*70)
print()
