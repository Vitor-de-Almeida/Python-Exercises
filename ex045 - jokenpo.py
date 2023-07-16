"""Create a program that makes the computer play jokenpo with you."""
from random import choice
n = str(input('\033[1;34m Computer you play "Jokenpo" with you. Write rock, paper or scissors to'
              ' play!\033[m ')).strip().lower()
r = 'rock'
p = 'paper'
s = 'scissors'
game = [r, p, s]
c = choice(game)
if c == r and n == r:
    print(f'\033[1;33m You tied with the computer! You chose {n} and the computer chose {c}. Try again!\033[m')
elif c == r and n == p:
    print(f'\033[1;32m You win against the computer! You chose {n} and the computer chose {c}. Congratulations!\033[m')
elif c == r and n == s:
    print(f'\033[1;31m You lost against the computer! You chose {n} and the computer chose {c}.Try again!\033[m')
#
elif c == p and n == r:
    print(f'\033[1;36m You lost against the computer! You chose {n} and the computer chose {c}.Try again!\033[m')
elif c == p and n == p:
    print(f'\033[1;35m You tied with the computer! You chose {n} and the computer chose {c}. Try again!\033[m')
elif c == p and n == s:
    print(f'\033[1;37m You win against the computer! You chose {n} and the computer chose {c}. Congratulations!\033[m')
#
elif c == s and n == r:
    print(f'\033[1;32m You win against the computer! You chose {n} and the computer chose {c}. Congratulations!\033[m')
elif c == s and n == p:
    print(f'\033[1;34m You lost against the computer! You chose {n} and the computer chose {c}.Try again!\033[m')
elif c == s and n == s:
    print(f'\033[1;37m You tied with the computer! You chose {n} and the computer chose {c}. Try again!\033[m')

