from random import randint

print('Sou seu computador!')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

computador = randint(0, 10)
jogador = int(input('Qual é o seu palpite? '))

while jogador != computador:
    if jogador < computador:
        print('Mais... tente novamente.')
    else:
        print('Menos... tente novamente.')
    jogador = int(input('Qual é o seu palpite? '))

print('Parabéns! Você adivinhou o número que eu pensei.')
