from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador == 0:
    print('Você jogou PEDRA.')
elif jogador == 1:
    print('Você jogou PAPEL.')
elif jogador == 2:
    print('Você jogou TESOURA.')
else:
    print('Jogada inválida!')

if computador == 0:
    print('O computador jogou PEDRA.')
elif computador == 1:
    print('O computador jogou PAPEL.')
else:
    print('O computador jogou TESOURA.')

if jogador == computador:
    print('EMPATE!')
elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
    print('VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU!')
