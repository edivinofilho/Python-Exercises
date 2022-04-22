# Exercise 13: Find the factorial of a given number

num = 10
fact = 1
print(f'{num}! = ', end='')
for c in range(num, 0, -1):
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    fact = fact * c
    c -= 1
print(fact)

