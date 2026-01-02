numero = int(input('Digite um número para calcular: '))
minimo = maximo = numero
soma = 0
cont = 1
pergunta = ''

while pergunta != 'N':
    soma += numero

    if pergunta == 'S':
        numero = int(input('Digite um número para calcular: '))
        cont += 1
        
        if numero > maximo:
            maximo = numero
        elif numero < minimo :
            minimo = numero

    elif pergunta == 'N':
        print('Fim do programa.')
    else:
        print('Opção inválida! Digite S ou N.')
    
    

    pergunta = input('Deseja continuar? [S/N] ').strip().upper()[0]

media = soma / cont

print('A soma dos números é:', soma)
print('O maior número é:', maximo)
print('O menor número é:', minimo)
print('A média dos números é: {:.2f}'.format(media))