# Sequência Fibonacci
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8...

num = int(input('Quantos termos da sequência de Fibonacci você quer? '))
n1 = 0
n2 = 1
cont = 3
print('0 → 1 → ', end='')
for c in range(0, num - 2):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(f'{n3} →', end=' ')
print('FIM')
