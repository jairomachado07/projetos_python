soma = cont = 0

while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1

print('A soma dos {} números é: {}'.format(cont, soma))