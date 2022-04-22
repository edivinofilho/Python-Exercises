# Empréstimo Bancário

casa = int(input('\nDigite o valor da casa a ser financiada R$ '))
tempo = int(input('Em quantos anos você gostaria de financiar? '))
salario = int(input('Digite o seu salário R$ '))
prestacao = casa / (tempo * 12)
limite = salario * 30 / 100
if prestacao > limite:
    print(f'\nO seu financiamento foi NEGADO. O valor da sua prestação seria R$ {prestacao:.2f}')
    print(f'Sua prestação poderia ser no máximo R$ {limite:.2f}, ou seja 30% do seu salário')
else:
    print(f'\nO seu empréstimo será concedido e sua prestação será de R$ {prestacao:.2f}')
    print(f'O seu limite de prestação seria R$ {limite:.2f}')
