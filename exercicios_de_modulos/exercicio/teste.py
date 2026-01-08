import moeda

preco = float(input("Digite o preço: "))
print(f'A metade de {preco} é {moeda.metade(preco, True)}')
print(f'O dobro de {preco} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
