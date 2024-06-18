# Isis de Oliveira Silva França
# Turma 0152
# Atividade 007
# Faça um programa que receba 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares.
import os


os.system('cls')

print('-'*70)
print('PAR E ÍMPAR:')
print('='*70)

# inicializando variaveis
lista = []
lista_par = []
lista_impar = []


for i in range(7):
    while True:
        numero = input('Digite um numero: ').strip()
        if numero.isdigit():
            numero = int(numero)
            if numero % 2 == 0:
                lista_par.append(numero)
            else:
                lista_impar.append(numero)
            break
        else:
            print('Informe um valor válido.')

print(f'A lista do números pares digitados é: {lista_par}')
print(f'A lista do números ímpares digitados é: {lista_impar}')
