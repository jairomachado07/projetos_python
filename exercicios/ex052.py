def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if passo == 0:
        passo = 1
    if inicio < fim:
        for n in range(inicio, fim + 1, passo):
            print(n, end=' ')
    else:
        for n in range(inicio, fim - 1, -passo):
            print(n, end=' ')
    print('FIM!')

contador(1, 10, 1)