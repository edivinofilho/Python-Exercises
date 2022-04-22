# Exercise 6: Count the total number of digits in a number

number = int(input('Enter a whole number to know the number of digits of it: '))
count = 0
while number != 0:
    number = number // 10
    count += 1
print(f'Your number has {count} digit(s)')
