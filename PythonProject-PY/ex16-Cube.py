# Exercise 16: Calculate the cube of all numbers from 1 to a given number

num = int(input('Number: '))
cube = 0
for c in range(1, num + 1):
    cube = c ** 3
    print(f'Current number is {c} and the cube is {cube}')
