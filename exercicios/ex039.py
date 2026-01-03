numeros = list()
for n in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {n}: ')))
print('-=-' * 10)
for n in numeros:
    print(f'Você digitou o valor {n} na posição {numeros.index(n)}')
print(numeros)