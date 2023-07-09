"""#Write a program that makes the computer "think" of an integer between 0 and 5 and
ask the user to try to figure out which number was chosen by the computer.
The program should write on the screen if the user won or lost."""
import random
from time import sleep

it = random.randint(1, 5)
n = int(input('Computer will chose an \033[1;033minteger\033[m between \033[34m 0 \033[mand \033[34m5\033[m. Try to'
              ' figure out which \033[1;33mnumber\033[m it has chosen:'))
print('\033[1;32mProcessing\033[m')
sleep(2)
if n == it:
    print(f'Congratulations, you win against computer! You guessed \033[1;34m{n}\033[m as computer did!')
else:
    print(f"Don't be sad, computer has chosen \033[1;34m{it}\033[m. Try again to win against the computer!")
