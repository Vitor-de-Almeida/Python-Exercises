"""Develop a program that reads four values from the keyboard and stores them in a Tuple. At the end, show:
a) How many times did the value 9 appear.
b) In what position was the first value 3 entered.
c) What were the even numbers."""
n1 = int(input('\033[1;36mEnter an integer:\033[m '))
n2 = int(input('\033[1;36mEnter another integer:\033[m '))
n3 = int(input('\033[1;33mEnter more one integer:\033[m '))
n4 = int(input('\033[1;33mEnter the last integer:\033[m '))
tp = (n1, n2, n3, n4)
print(f'\033[1;34mYou entered the values {tp}\033[m')
print(f'\033[1;97mThe number 9 appear {tp.count(9)} times!\033[m')
if 3 in tp:
    print(f'\033[1;37mThe number 3 appear in the position {tp.index(3)+1}ª !\033[m')
else:
    print(f'\033[1;37mThe number 3 were not entered for any position!\033[m')
print(f'\033[1;34mThe entered even numbers are\033[m', end='')
count = 0
for c in range(0, 4):
    if tp[c] % 2 == 0:
        print(f'\033[1;34m {tp[c]} \033[m', end='')
        count += 1
if count == 0:
    print(f'\033[1;34m missing\033[m', end='')


