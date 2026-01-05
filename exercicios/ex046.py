matriz = [], [], []
spar = mai = scol = 0

for c in range(0, 3):
    for l in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {l}]: ')))
print('-=' * 20)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^3}]', end='')
        if matriz[c][l] % 2 == 0:
            spar += matriz[c][l]
    print()
print('-=' * 20)
for c in range(0, 3):
    scol += matriz[c][2]
    if c == 0:
        mai = matriz[c][0]
    else:
        if matriz[c][0] > mai:
            mai = matriz[c][0]
            
for c in range(0, 3):
    if matriz[c][0] > mai:
        mai = matriz[c][0]

print('-=' * 20)
print(f'A soma dos valores pares é {spar}.')
print(f'A soma dos valores da terceira coluna é {scol}.')
print(f'O maior valor da primeira linha é {mai}.')