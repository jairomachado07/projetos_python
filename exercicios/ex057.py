def leiaint(msg):
    ok = False
    valor = 0
    while not ok:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("Valor inválido. Digite um número inteiro.")
    return valor

#programa principal
n = leiaint("Digite um número: ")
print(f"Você digitou o número {n}.")