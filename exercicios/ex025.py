sexo = ''
while sexo not in ['M', 'F']:
    sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
    if sexo not in ['M', 'F']:
        print('Escreva M para masculino ou F para feminino.')
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso.')
elif sexo == 'F':
    print('Sexo Feminino registrado com sucesso.')