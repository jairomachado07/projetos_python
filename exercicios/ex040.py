listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('-=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor foi {mai} na posição {listanum.index(mai)}')
print(f'O menor valor foi {men} na posição {listanum.index(men)}')
