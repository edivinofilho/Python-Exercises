"""
Exercise 2: Print the following pattern

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
rows = 5
for a in range(1, rows + 1):  # rows
    for b in range(1, a + 1):  # columns
        print(b, end=' ')
    print('')
