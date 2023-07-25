"""Develop a program that reads the first term and ratio of an AP. At the end, show the first 10 terms of this progression.
If the user want to see more terms, you need to show them"""
t = int(input('\033[1;34mEnter the first term of the arithmetic ratio: \033[m'))
r = int(input('\033[1;32mEnter the ratio of the arithmetic ratio: \033[m'))
n = 11
b = 0
c = 0
d = 1
while n != c:
    AR = t + r*b
    print(f'\033[1;97m{AR}\033[m', end=' -> ')
    b = b + 1
    n = n - 1
    if n == d:
        duv = str(input('\nYou want to see more terms? [S/N]')).strip().lower()[0]
        if duv == 's':
            m = int(input('Enter how many more terms do you want to see: '))
            n = b + m
            c = n - m
            d = c
print('\033[1;33m\nThank you!\033[m')
