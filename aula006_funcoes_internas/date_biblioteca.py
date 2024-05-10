# importando as bibliotecas
import os
#importando as funções que queremos utilizar
from datetime import datetime
from datetime import date


#limpando o terminal
os.system('cls')

# declarando a variavel para data
data = datetime.now() # como se estivessemos tipando a variavel/ tipo criamos um objeto

#declarando uma variável data formatada
data_formatada = data.strftime('%d/%m/%Y')

# declarando uma variavel data e hora formatada
data_hora_formatada = data.strftime('%d/%m/%Y %H:%M')

print(f'Data formatada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatada}')

#recebendo o ano
data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

#imprimindo a data atual e o nascimento
print('-'*70)
print(f'Data atal no sistema: {data_atual}')
print(f'Nascimento..........: {nascimento}')
#imprimindo só o ano
print(f'Ano atual...........: {data_atual.year}')
#imprimindo só a idade
print(f'Sua idade é ........: {idade} anos')
print('-'*70)