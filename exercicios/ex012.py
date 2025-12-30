preço = float(input('Preço do produto: R$'))
novo = preço - (preço * 5 / 100)
print('O preço do produto que custava {:.2f},passa a custar com 5% de desconto o valor de: R${:.2f}'.format(preço,novo))