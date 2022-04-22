# Exercise 12: Display Fibonacci series up to 10 terms

n1 = 0
n2 = 1
n3 = 1
print('Fibonacci: 0 1', end=' ')
for c in range(0, 8):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=' ')
print('The End!')
