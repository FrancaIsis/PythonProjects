# Curso de Desenvolvimento de Sistemas
# Turma 0152 (Braba)
# Autor: Isis
# Data: 25/04/2024
# Atividade 002: Condicionais

# C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade para ajudar a promover a segurança nas estradas.
# Eles precisam de um programa que permita aos usuários inserir a velocidade de um carro e, em seguida, exibir na tela uma mensagem
# adequada com base na velocidade fornecida. O objetivo principal é alertar os motoristas caso ultrapassem o limite de velocidade de 60 km/h,
# incentivando-os a dirigir dentro dos limites legais e, assim, reduzir o risco de acidentes.

# importando as bibliotecas
import os


# limpando os dados do terminal
os.system('cls')

print('-'*70)
print('RADAR')
print('='*70)

# inicializando as variaveis
velocidade_automovel = 0
velocidade_limite = 60

# entrada de dados
velocidade_automovel = int(input('Informe a velocidade do veículo: '))
print()

# processamento de dados/ saída
if velocidade_automovel < 60:
    print(f'Parabéns motorista!! Sua velocidade atual é de {velocidade_automovel} km/h. '
          f'Você está abaixo do limite de {velocidade_limite} km/h')
elif velocidade_automovel == 60:
    print(f'Cuidado motorista!! Sua velocidade atual é de {velocidade_automovel} km/h. '
          f'Você está no LIMITE de {velocidade_limite} km/h')
else:
    print(f'Já era motorista! Sua velocidade atual é de {velocidade_automovel} km/h. '
          f'Você ultrapassou o limite de {velocidade_limite} km/h. Em breve receberá uma multa em sua residência.')
    
print('-'*70)
print('Fim do programa')
print('='*70)
