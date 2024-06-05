# Isis de Oliveira Silva França
# Turma 0152
# Atividade 005
# Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

import os


os.system('cls')

print('-'*70)
print('Banco de dados fake')
print('='*70)
print('')

#Inicializando variaveis
usuario = 'admin'
senha = '1234'



while True:
    usuario_digitado = input('Digite o usuário: ')
    senha_digitada = input('Digite a senha: ')
    if usuario == usuario_digitado and senha == senha_digitada:
        print('Ok, tudo certo!')
        break
    