def escreva (msg):
    tam = len(msg)
    print('-' * (tam + 4))
    print(f'  {msg}')
    print('-' * (tam + 4))

escreva(input('Digite sua mensagem: '))

