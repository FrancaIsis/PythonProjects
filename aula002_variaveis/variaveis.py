#primeira aula sobre variaveis
#importando biblioteca para o clear
import os

#limpando o terminal
os.system('cls')

print('-'*70)
print('Estudo de variáveis')
print('-'*70)

#atenção para os nomes das variaveis
nome = 'Isis'
nascimento = 1985
altura = 1.49
peso = 45.6
doador = False
complexo = 3j
PI = 3.14 #constante toda em maiuscula

#mostrando os tipos das variaveis na tela

print('-'*70)
print('Tipos das variaveis:')
print('-'*70)
print('A variavel nome - ',nome,'- é do tipo ', type(nome))
print('A variavel nascimento - ',nascimento,'- é do tipo ', type(nascimento))
print('A variavel altura - ',altura,'- é do tipo ', type(altura))
print('A variavel peso - ',peso,'- é do tipo ', type(peso))
print('A variavel doador - ',doador,'- é do tipo ', type(doador))
print('A variavel PI - ',PI,'- é do tipo ', type(PI))
print('-'*70)
print('')