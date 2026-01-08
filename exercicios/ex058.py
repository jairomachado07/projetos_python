def LeiaInt(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("\033[31mErro! Digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário interrompeu a entrada.\033[m")
            return None
        else:
            return n

num = LeiaInt("Digite um número inteiro:")
print(f"Você digitou o número {num}.")
