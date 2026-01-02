print('-'*30)
print('Sequência de Fibonacci:')
print('-'*30)

fibonacci = int(input("Digite um numero para ver os termos da sequencia de Fibonacci: "))
numero = 0
numero2 = 1
cont = 2

print(f"{numero} {numero2}", end=' ')

while cont <= fibonacci:
    numero3 = numero + numero2
    print(numero3, end=' ')
    numero = numero2
    numero2 = numero3
    cont += 1

print('\nFIM')
print('-'*30)
