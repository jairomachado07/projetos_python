larg = float(input('Largura da parede (m): '))
alt = float(input('Altura da parede (m): '))
area = larg * alt
tinta = area / 2
print('Sua parede tem dimenção de {} x {} A área da parede é de {} m².'.format(larg, alt, area))
print('A quantidade de tinta necessária para pintar a parede é de {} litros.'.format(tinta))

