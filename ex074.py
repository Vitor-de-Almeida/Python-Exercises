"""Make a program that generates five random numbers and put it into a tuple.
After that, show on the screen the list of numbers generated show the lowest and highest number in the tuple"""
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'\033[1;34mThe generated numbers are:\033[m', end=' ')
for t in n:
    print(f'\033[1;34m{t}\033[m', end=' ')
print(f'\n\033[1;36mThe highest number is: {sorted(n)[4]}\033[m')
print(f'\033[1;31mThe lowest number is: {sorted(n)[0]}\033[m')


