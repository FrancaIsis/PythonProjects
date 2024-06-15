# Isis de Oliveira Silva França
# Turma 0152
# Atividade 006
# Ler uma lista com 10 números, depois apresente o maior e o menor número da lista
import os


os.system('cls')

print('-'*70)
print('MAIOR E MENOR:')
print('='*70)

# inicializando variaveis
lista = []
numeros = 0
maior = 0
#menor = 0

# entrada de dados
for i in range(10):
    while True: # validação
        numeros = input('Digite um número:')
        
        if numeros.isdigit():
            numeros = int(numeros) # casting
            menor = numeros
            lista.append(numeros)
            break
        else:
            print('Informe um valor válido.')

for i in lista:
    if i < menor:
        menor = i
    if i > maior:
        maior = i

print(f'A lista digitada por você foi {lista}')
print(f'O menor número dessa lista é {menor} e o maior é {maior}')
