números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Número duplicado! Não vou adicionar...')
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp in 'nN':
        break
print('-=' * 30)
números.sort()
print('você digitou os valores', (números))

