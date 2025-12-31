num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('1 - Converter para binário')
print('2 - Converter para octal')
print('3 - Converter para hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} em binário é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
