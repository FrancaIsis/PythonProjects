#verificar numero maior e numero menor
import os


os.system('cls')

#inicializando as variaveis
n1 = 0
n2 = 0
n3 = 0
maior = 0
menor = 0

#entrada de dados
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input( 'Informe o terceiro numero: '))

#processoamento
if n1 == n2 == n3:
    print('Os números são iguais. ')
elif n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3


if n1 < n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

#saida
print(f'Os números informados foram: {n1}, {n2}, {n3}. O maior deles é {maior}')

