# Exercise 17: Find the sum of the series upto n terms.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

n = int(input('Choose a whole number for the amount of times you want to see the series: '))
start = int(input('Choose the number you want the pattern from: '))
set_start = start
sum_seq = 0
for c in range(0, n):
    print(start, end=' ')
    print('=' if c == (n-1) else '+', end=' ')
    sum_seq += start
    start = start * 10 + set_start
print(sum_seq)
