"""make a program that shows on the screen the countdown for the new year celebrations.
The program must start at ten seconds and go to 0 seconds."""
from time import sleep
s = 1
print('\033[1;30;107mWelcome to the new year celebrations!\033[m')
for c in range(10, 0, -1):
    print(f'\033[1;97;40m {c} seconds!\033[m')
    sleep(1)
print('\033[1;34;43mHappy New Year Everyone!\033[m')


