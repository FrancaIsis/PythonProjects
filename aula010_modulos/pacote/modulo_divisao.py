def dividir(a, b):
    """Método para dividir 2 numeros

    Args:
        a (_type_): dividendo
        b (_type_): divisor
    Returns:
        str: Mensagem de erro ou OK se a divisão for bem sucedida
        any: Quociente ou None em caso de erro
    """
    if b == 0:
        return None, 'Erro de divisão'
    else:
        divisao = a / b
        return divisao, 'OK!'
