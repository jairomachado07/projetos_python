from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor entre 0 e 10: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = input('Você quer Par ou Ímpar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...\n')
print('GAME OVER! Você venceu {} vezes.'.format(v))