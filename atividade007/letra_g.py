# Faça um programa que sorteia os números da Mega Sena e da Lotofácil
# Para o sorteio dos 6 números da Mega-Sena é utilizado 1 globo, carregado com bolas numeradas de 01 a 60.
# Para o sorteio dos 15 números da Lotofácil é utilizado 1 globo, carregado com bolas numeradas de 01 a 25

import os
import random


# limpando dados
os.system('cls')

print('-'*70)
print('SORTEIO')
print('='*70)

# inicializando variaveis
lista_mega_sena = []
lista_lotofacil = []
lista_aposta_mega = []
lista_aposta_loto = []
contador = 0


while True:
    opcao = input('Escolha uma opção:\n'
                  'Digite 1 - Mega Sena\n'
                  'Digite 2 - Lotofácil\n'
                  'Digite 0 - SAIR\n')
    if opcao.isdigit():
        opcao = int(opcao)
        while opcao == 1 or opcao == 2:  # se o usuario digitar qq outro numero irá saír do loop

            if opcao == 1:
                # entrada de dados Mega Sena
                for i in range(6):  # loop para solicitar 6 numeros ao usuario
                    while True:
                        aposta = input('Digite um número de entre 1 e 60: ')
                        if aposta.isdigit():  # verifica se o valor digitado é um numero
                            # realiza um casting para inteiro
                            aposta = int(aposta)
                            if aposta > 0 and aposta <= 60:
                                if aposta not in lista_aposta_mega:  # não apostar numeros repetidos
                                    lista_aposta_mega.append(aposta)
                                    break
                                else:
                                    print('Você já informou esse valor.')
                            else:
                                print('Informe um valor entre 1 e 60.')
                        else:
                            print('Digite um número válido.')

                print(f'\nOs números escolhidos foram: {lista_aposta_mega}')

                # sorteando os numeros
                print('-'*70)
                print('SORTEIO')
                print('='*70)

                for i in range(6):  # loop para sortear 6 numeros
                    # sample serve para retornar valores unicos de uma população, passando o paramento de qtos valores unicos queremos
                    sorte = random.sample(range(1,61), 6)
                print(f'\nOs números sorteados foram: {sorte}')
                print('-'*70)

                # verificando o numero de acertos
                for i in lista_aposta_mega:
                    for j in sorte:
                        if i == j:
                            contador += 1
                            lista_mega_sena.append(i)

                # resultado
                print(
                    f'Você acertou {contador} numeros da Mega Sena - >{lista_mega_sena}')
                print('-'*70)

            if opcao == 2:
                # entrada de dados Loto
                for i in range(15):  # loop para solicitar 6 numeros ao usuario
                    while True:
                        aposta = input('Digite um número de entre 1 e 25: ')
                        if aposta.isdigit():
                            aposta = int(aposta)
                            if aposta > 0 and aposta <= 25:
                                if aposta not in lista_aposta_loto:  # não apostar numeros repetidos
                                    lista_aposta_loto.append(aposta)
                                    break
                                else:
                                    print('Você já informou esse valor.')
                            else:
                                print('Informe um valor entre 1 e 25.')
                        else:
                            print('Digite um número válido.')

                print(f'\nOs números escolhidos foram: {lista_aposta_loto}')

                # sorteando os numeros
                print('-'*70)
                print('SORTEIO')
                print('='*70)

                for i in range(15):  # loop para sortear 15 numeros
                    # sample serve para retornar valores unicos de uma população, passando o paramento de qtos valores unicos queremos
                    sorte = random.sample(range(1,26), 15)
                print(f'\nOs números sorteados foram: {sorte}')
                print('-'*70)

                # verificando o numero de acertos
                for i in lista_aposta_loto:
                    for j in sorte:
                        if i == j:
                            contador += 1
                            lista_lotofacil.append(i)
                # resultado
                print(
                    f'Você acertou {contador} numeros da LotoFacil - > {lista_lotofacil}')

            # repete o menu
            print('-'*70)
            opcao = int(input('Escolha uma opção:\n'
                              'Digite 1 - Mega Sena\n'
                              'Digite 2 - Lotofácil\n'
                              'Digite 0 - SAIR\n'))
        break
    else:
        print()
        print('Informe um valor válido')
