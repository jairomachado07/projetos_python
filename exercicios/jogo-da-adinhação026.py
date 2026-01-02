from random import randint
from time import sleep

print('Sou seu computador!')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

computador = randint(0, 1000)
jogador = 500
minimo = 0
maximo = 1000
contador = 0

while jogador != computador:
    if jogador < computador:
        if(maximo - minimo) < 2:
            jogador -= 1
        else:
            minimo = jogador
            jogador = ((minimo + maximo+1) // 2)
                
    else:
        if(maximo - minimo) < 2:
            jogador += 1
        else:
            maximo = jogador
            jogador = ((minimo + maximo) // 2)
        
    contador += 1
    print(f'Você ainda não acertou. Seu palpite foi {jogador}.')
    print(minimo, maximo, contador, computador)
    sleep(4)

print(f'Seu palpite foi {jogador}.')
print('Parabéns! Você adivinhou o número que eu pensei.')
