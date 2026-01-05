matriz = [], [], []

for c in range(0, 3):
    for l in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {l}]: ')))
print('-=' * 20)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^3}]', end='')
    print()
print('-=' * 20)