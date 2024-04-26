# Curso de Desenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis
# Data: 25/04/2024
# Atividade 002: Condicionais

#B) A empresa "DataMax" está desenvolvendo um novo software de análise estatística e precisa de uma funcionalidade
# que permita aos usuários inserir três números e, em seguida, exibir na tela qual é o maior número, 
# qual é o menor número ou se os números são todos iguais. Essa funcionalidade é crucial para os analistas de dados da 
# "DataMax" que trabalham com conjuntos de dados diversos e precisam rapidamente identificar as características básicas desses conjuntos, 
# como a presença de outliers ou a uniformidade dos números.

#importando bibliotecas
import os


#limpando os dados do terminal
os.system('cls')

print('-'*70)
print('VERIFICANDO 3 NÚMEROS')
print('='*70)

# inicializando as variaveis
primeiro_numero = 0
segundo_numero = 0
terceiro_numero = 0

#entrada de dados
primeiro_numero = int(input('Digite o primeiro número: '))
print('')
segundo_numero = int(input('Digite o segundo número: '))
print('')
terceiro_numero = int(input('Digite o terceiro número: '))
print('')

#processamento / saída de dados
if (primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero):
    print(f'O número {primeiro_numero} é maior que {segundo_numero} e {terceiro_numero}')
elif(segundo_numero > primeiro_numero and segundo_numero > terceiro_numero):
    print(f'O número {segundo_numero} é maior que {primeiro_numero} e {terceiro_numero}')
elif(terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero):
    print(f'O número {terceiro_numero} é maior que {primeiro_numero} e {segundo_numero}')
elif primeiro_numero == segundo_numero == terceiro_numero:
    print(f'Os números {primeiro_numero}, {segundo_numero} e {terceiro_numero} são iguais!')
    
print('-'*70)
print('Fim do programa')
print('='*70)