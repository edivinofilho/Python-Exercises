# Exercise 4: Write a program to print multiplication table of a given number

num = int(input('Enter a whole number: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c}')
