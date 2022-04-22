# Programa que leia um número inteiro e mostre seu fatorial:
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número inteiro: '))
c = num
f = c
print(f'{num}! = {num} x ', end='')
while c > 1:
    c -= 1
    f = f * c
    print(f'{c}', 'x' if c > 1 else '=', end=' ')
print(f'{f}')
