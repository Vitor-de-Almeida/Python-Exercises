"""Write a program that plays even or odd with the computer.
The game will only be interrupted when the player loses,
showing the total number of consecutive victories he has achieved at the end of the game"""
from random import randint
count = 0
result = ''
even = 'even'
odd = 'odd'
print('\033[1;37m=-=\033[m'*14)
print('\033[1;97;40m Lets play Even or Odd with the computer!\033[m')
while True:
    comp = randint(1, 26)
    print('\033[1;37m=-=\033[m' * 14)
    n = int(input('\033[1;34mEnter any number you want to play even or odd with the computer:\033[m'))
    pi = str(input('\033[1;32mYou want Even or Odd?[E/O]:\033[m')).strip().lower()[0]
    if (n + comp) % 2 == 0:
        result = even
    else:
        result = odd
    if pi == result.strip().lower()[0]:
        print('\033[1;37m=-=\033[m' * 13)
        print(f'\033[1;36mYou choose {n} and the computer {comp}. The total are {n+comp} and the game '
              f'was {result}!\033[m')
        print('\033[4;35mYou win. Lets play again!')
    else:
        print('\033[1;37m=-=\033[m' * 13)
        print(f'You choose {n} and the computer {comp}. The total are {n + comp} and the game was {result}')
        print(f'\033[4;35mYou lost. Game Over. You win {count} times!')
        print('\033[1;37m=-=\033[m' * 13)
    count += 1
    if pi != result.strip().lower()[0]:
        break



