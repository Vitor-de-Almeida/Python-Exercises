"""Develop a program that reads the first term and ratio of an AP. At the end, show the first 10 terms of this progression."""
t = int(input('\033[1;34mEnter the first term of the arithmetic ratio: \033[m'))
r = int(input('\033[1;32mEnter the ratio of the arithmetic ratio: \033[m'))
n = 10
b = 0
while n != 0:
    AR = t + r*b
    print(f'\033[1;97m{AR}\033[m', end=' -> ')
    b = b + 1
    n = n - 1
print('\033[1;33m\nEND\033[m')
