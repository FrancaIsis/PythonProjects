# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 02/06/2024.
# G) Faça um programa que calcule os números primos em um 
# intervalo pré-determinado pelo usuário.

# Importando as bibliotecas do sistema.
import os


# Limpando o terminal.
os.system('cls')

# Imprimindo título.
print('.'*79)
print('NÚMEROS PRIMOS')
print('.'*79)

# Entrada de dados.
while True:
    print('.'*79)
    print('!AVISOS!')
    print('Por favor digite sempre um nº a mais no final do seu intervalo')
    print('Números menores que dois são inválidos.')
    print('Porque dois é o menor número primo.')
    print('.'*79)
    print('-'*79)
    inicio = input('Digite o início do seu intervalo: ')
    final = input('Digite o final do seu intervalo: ')
    print('-'*79)
    
    # Validação da entrada.
    if not(inicio.isnumeric() and final.isnumeric()):
        print('Entrada inválida.')
        print('Por favot digite um número.')
    else:
        break

# Declarações de variáveis.
primos = []
primo = bool

# Processamento de dados.
for i in range(int(inicio), int(final)): # For para gerar o intervalo de números.
    primo = True # Flag que afirma que o número é primo.
    for j in range (int(inicio), i): # For que gera os números do inicio do intervalo a i.
        if i % j == 0: # Verifica se o nº i dividido por j gera o resto 0.
            primo = False # Se sim diz que não é primo.
            break # Para o looping pois o número não é primo.
    if primo: # Se primo ainda for True.
        primos += [i] # Adiciona i a lista de primos.

# Saída de dados.
print('='*79)
print(f'Os nº primos no intervalo de {inicio} a {final} são:')
print(primos)
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)