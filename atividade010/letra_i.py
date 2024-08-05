# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024

# Faça um programa de perguntas e respostas sobre os estados e capitais brasileiras. 
# O programa deverá exibir para o usuário o está e perguntar qual a sua capital. 
# Se o usuário errar a resposta, o programa será finalizado apresentando quantas perguntas estão corretas. 
# Utilize ao menos uma função e não há a necessidade de modularizar o código.

import os
import random


os.system('cls')

print('-'*70)
print('ESTADOS BRASILEIROS')
print('='*70)

contador = 0
dicionario_estados = {'Acre': 'rio branco',
    'Alagoas': 'maceió',
    'Amapá': 'macapá',
    'Amazonas': 'manaus',
    'Bahia': 'salvador',
    'Ceará': 'fortaleza',
    'Distrito Federal': 'brasília',
    'Espírito Santo': 'vitória',
    'Goiás': 'goiânia',
    'Maranhão': 'são luís',
    'Mato Grosso': 'cuiabá',
    'Mato Grosso do Sul': 'campo grande',
    'Minas Gerais': 'belo horizonte',
    'Pará': 'belém',
    'Paraíba': 'joão pessoa',
    'Paraná': 'curitiba',
    'Pernambuco': 'recife',
    'Piauí': 'teresina',
    'Rio de Janeiro': 'rio de janeiro',
    'Rio Grande do Norte': 'natal',
    'Rio Grande do Sul': 'porto alegre',
    'Rondônia': 'porto velho',
    'Roraima': 'boa vista',
    'Santa Catarina': 'florianópolis',
    'São Paulo': 'são paulo',
    'Sergipe': 'aracaju',
    'Tocantins': 'palmas'}

estado = ''
capital = ''


def quiz_estados(estado, capital):
    resposta = input(f'Qual é a capital do {estado}?\n').lower()
    if resposta == capital:
        contador = 1
        print('Parabéns! Continue assim!\n')
    else:
        contador = 0
        print(f'Xih ! resposta erradada, a capital correta era {capital}!\n')
    return contador
    
while True:
    estado, capital = random.choice(list(dicionario_estados.items()))
    resultado = quiz_estados(estado,capital)
    if resultado == 1:
        contador += 1
    else:
        print(f'Você acertou {contador} capitais!!')
        break
