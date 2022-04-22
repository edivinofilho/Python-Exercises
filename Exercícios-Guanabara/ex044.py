# Valor da compra e condições de pagamento

compra = float(input('\nDigite o valor total da sua compra R$ '))
print('''
Condições de pagamento: 
[1] À vista em dinheiro/cheque → 10% de desconto
[2] À vista no cartão → 5% de desconto
[3] Em 2X no cartão → sem juros
[4] Em 3X ou mais no cartão → 20% de juros
''')
opcao = int(input('Forma de pagamento: '))
if opcao == 1:
    desconto = compra * 10 / 100
    print('Você recebeu 10% de desconto.')
    print(f'O valor do seu desconto será de R$ {desconto:.2f}')
    print(f'O valor da sua compra, com disconto, será de R$ {compra - desconto:.2f}')
elif opcao == 2:
    desconto = compra * 5 / 100
    print(f'Você recebeu 5% de desconto.')
    print(f'O valor do seu desconto será de R$ {desconto:.2f}')
    print(f'O valor da sua compra, com disconto, será de R$ {compra - desconto:.2f}')
elif opcao == 3:
    print(f'Sua compra será parcelada em 2X no cartão, sem juros. Cada prestação será de R$ {compra / 2:.2f}')
elif opcao == 4:
    vezes = int(input('Em quantas vezes você gostaria de parcelar? '))
    juros = compra * 20 / 100
    print(f'Sua compra será divida em {vezes} vezes e será adicionada 20% de juros.')
    print(f'O valor total da sua compra com juros será de R$ {compra + juros:.2f}')
    print(f'Cada prestação será de R$ {(compra + juros) / vezes:.2f}')
else:
    print('Esta opção não existe.')
