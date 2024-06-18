# Isis de Oliveira Silva França
# Turma 0152
# Atividade 007
#Após esta entrada de dados, faça o seguinte:
#• Mostre a quantidade de notas que foram lidas.
#• Exiba todas as notas na ordem em que foram informadas.
#• Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
#• Calcule e mostre a soma das notas.
#• Calcule e mostre a média das notas.

# importando biblioteca
import os


# limpando dados
os.system('cls')

print('-'*70)
print('NOTAS')
print('='*70)

# inicializando variaveis
notas = []
soma = 0
media = 0
contador = 0


while True:
    n = input('Informe a nota. Digite s ou 0 para SAIR: ').lower().strip()
    if n == 's' or n == '0':
        break

    else:
        if n.isdigit():
            n = int(n)
            notas.append(n)
            soma = soma + n
            contador += 1
        else:
            print('Informe um valor válido.')

media = soma/contador
print('='*70)
print(f'O número de notas lidas foi: {len(notas)}')
notas.sort()
print(f'As notas informadas foram: {notas}')
notas.sort(reverse=True)
print('As notas informadas em ordem inversa foram: ')

for i in (notas):
    print(f'{i}\n')
print(f'A soma das notas é: {soma}')
print(f'A media das notas é {media}')