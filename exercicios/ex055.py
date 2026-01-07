def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de n.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(i, end=' ')
            if i > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f


#programa principal
print(fatorial(5, show=True))
help(fatorial)