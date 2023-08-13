"""Make a program that reads five integers and take them into a list.
At the end, show on the screen which one was the greatest and the lowest and the position of every number."""
number = []
nb = 0
nl = 0
for c in range(0, 5):
    number.append(int(input('Enter an integer: ')))
    if c == 0:
        nb = nl = number[c]
    else:
        if number[c] > nb:
            nb = number[c]
        elif number[c] < nl:
            nl = number[c]
print('=-='*12)
print(f'\033[1;97mYou entered the list {number}\033[m')
print('=-='*12)
print(f'\033[1;34mThe biggest number is {nb} and his respective position is \033[m', end='')
for pos in range(0, len(number)):
    if number[pos] == nb:
        print(f'\033[1;34m{pos}...\033[m', end='')
print(f'\033[1;33m\nThe lowest number is {nl} and his respective position is \033[m', end='')
for pos in range(0, len(number)):
    if number[pos] == nl:
        print(f'\033[1;33m{pos}...\033[m', end='')

