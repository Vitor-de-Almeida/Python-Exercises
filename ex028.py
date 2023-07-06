"""#Write a program that makes the computer "think" of an integer between 0 and 5 and
ask the user to try to figure out which number was chosen by the computer.
The program should write on the screen if the user won or lost."""
import random
it = random.randint(1, 5)
n = int(input('Computer chose an integer number between 0 and 5. Try to figure out which number it has chosen:'))
if n == it:
    print('Congratulations, you win! You guessed right the number!')
else:
    print("Don't be sad, you didn't guessed correctly the right number. Try again!")
print(f'The number choosed by the computer is {it}')

