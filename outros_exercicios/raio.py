#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# area = pi*r²
print('-'*100)
print('Calculando a área de um circulo')
print('-'*100)

#inicializando as variaveis
PI = 3.14
raio = 0
area = 0.0

#coletando dados do usuario
raio = int(input('Informe o valor do raio: '))

#calculando o valor da area
area = PI*raio**2

#Imprimindo na tela

print(f'A área do círculo é {area}')
