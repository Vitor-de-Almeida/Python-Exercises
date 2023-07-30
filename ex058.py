"""#Write a program that makes the computer "think" of an integer between 0 and 10 and
ask the user to try to figure out which number was chosen by the computer.
The player must try until he guess the number."""
from random import randint
count = 1
number = randint(0, 10)
print('\033[1;32mI am your computer... I am just thought about a number between 0 and 10...\033[m')
p = int(input('\033[1;34mTry to figure out what number computer are thinking of:\n\033[m'))
while number != p:
    p = int(input('\033[1;32mTry again. What number computer are thinking of:\n\033[m'))
    if p < number:
        print('\033[4;33mMore... try again!...\033[m')
    elif p > number:
        print('\033[4;33mLess... try again!...\033[m')
    count += 1
print(f'\033[4;36mCongratulations. You needed {count} times to guess it right. Computer was thinking of {number}!\033[m')

