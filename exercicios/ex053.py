from time import sleep

def maior(*num):
    count = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'  {valor}', end=' ')
        sleep(0.5)
        if valor > maior:
            maior = valor
            count = 1
        elif valor == maior:
            count += 1
    print(f'\nO maior valor foi {maior} e apareceu {count} vez(es).')

maior(3, 5, 7, 2, 5, 7, 8, 8, 8)
maior(1, 2, 3)
maior(9, 7, 5, 3, 1)