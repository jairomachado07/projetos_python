casa = float(input('Valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}.'.format(prestacao))
if prestacao > minimo:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
