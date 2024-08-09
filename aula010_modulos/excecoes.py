# ZeroDivisionError
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('Erro: Divisão por zero!')
    
# ValuesError
try:
    numero = int('não é um número')
except ValueError:
    print('Erro: Valor inválido!')
    
# TypeError
try:
    soma = '5' + 5
except TypeError:
    print('Erro: Tipo de dado incompatível!')
    
# IndexError
lista = [1, 2, 3]
try:
    item = lista[5]
except IndexError:
    print('Erro: Índice fora do intervalo da lista!')
    
# KeyError
dicionario = {'chave':'valor'}
try:
    valor = dicionario['chave_inexistente']
except KeyError:
    print('Erro: Chave não encontrada no dicionário!')

#FileNotFoundError
try:
    with open('arquivo_inexistente.txt','r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print('Erro: Arquivo não encontrado!')

# IOError
try:
    with open('arquivo.txt','w') as arquivo:
        conteudo = arquivo.read()
except IOError:
    print('Erro: Operação de E/S falhou!')
    
# AtributeError
class Exemplo:
    def __init__(self):
        self.atributo = 'valor'

objeto = Exemplo()
try:
    print(objeto.atributo_inexistente)
except AttributeError:
    print('Erro: Atributo não encontrado no objeto!')
    
# importError
try:
    import modulo_inxistente #type: ignore - ignore o erro
except ImportError:
    print('Erro: Módulo não encontrado!')

# RuntimeError

try:
    raise RuntimeError('Este é um erro de exceção!')
except RuntimeError as e:
    print(f'Erro: {e}')
