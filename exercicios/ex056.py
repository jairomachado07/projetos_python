def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

#programa principal
n = str(input("Nome do jogador: "))
g = str(input("Número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

