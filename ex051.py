"""Develop a program that reads the first term and ratio of an AP. At the end, show the first 10 terms of this progression."""
t = int(input('\033[1;34mEnter the first term of the arithmetic ratio: \033[m'))
r = int(input('\033[1;32mEnter the ratio of the arithmetic ratio: \033[m'))
s = -1
for c in range(1, 11):
    s = s + 1
    AR = t + r*s
    print(f'{AR}')




