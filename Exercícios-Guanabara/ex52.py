# Faça um programa que leia um número inteiro e diga se ele é, ou não, um número primo.

num = int(input('\nDigite um número inteiro para saber se ele é, ou não, um número primo: '))
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print(f'O número {num} É um número primo, pois é dividio apenas por ele mesmo e pelo número UM.')
else:
    print(f'O número {num} NÃO é um número primo, pois ele é divisível por {cont} números.')
