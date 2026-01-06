def area(largura, altura):
    a = largura * altura
    print(f'A área de um terreno {largura}m x {altura}m é {a}m²')
    
#programa principal
print('Contole de terrenos')
largura = float(input('Largura (m): '))
altura = float(input('Altura (m): '))
area(largura, altura)
