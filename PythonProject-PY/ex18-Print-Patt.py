"""
Exercise 18: Print the following pattern
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
Hint: Use two for loops (One for each part of the pattern)
"""
rows = 5
for a in range(0, rows):  # rows
    for b in range(0, a + 1):  # columns
        print('*', end=' ')
    print('\r')

for a in range(rows, 0, -1):
    for b in range(0, a - 1):
        print('*', end=' ')
    print('\r')
