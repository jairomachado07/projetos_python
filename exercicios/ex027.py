numero = int(input("Digite um numero para o cauculo de fatorial: "))
c = numero
fatorial = 1

while c > 0:
    fatorial *= c

    if c > 1:
        print(c, end=' x ')
    elif c == 1:
        print(c)

    c -= 1
    
print(f"O fatorial de {numero} é {fatorial}")