# Exercise 3: Calculate the sum of all numbers from 1 to a given number

num = int(input('Enter a whole number: '))
add = 0
count = 0
for count in range(1, num + 1):
    add += count
    print(add)
