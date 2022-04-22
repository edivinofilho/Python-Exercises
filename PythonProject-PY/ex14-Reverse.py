# Exercise 14: Reverse a given integer number

num = int(input('Number: '))
rev_num = 0
while num > 0:
    reminder = num % 10
    rev_num = rev_num * 10 + reminder
    num = num // 10
print(rev_num)
