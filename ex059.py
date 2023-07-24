"""Make a program that reads two integers and show a menu on the screen:
[1] - Add
[2] - Multiply
[3] - Bigger
[4] - New numbers
[5] - Leave the program
Your program should resolve the option selected
"""
from time import sleep
n1 = float(input('\033[1;32mEnter the first number: \033[m'))
n2 = float(input('\033[1;32mEnter the second number: \033[m'))
soma = 0
end = 2
while end != 0:
    op = int(input('\033[1;34mChose the option you want:\n[1] - Add\n'
                   '[2] - Multiply\n'
                   '[3] - Bigger\n'
                   '[4] - New numbers\n'
                   '[5] - Leave the program\033[m\n'))
    if op == 1:
        soma = n1 + n2
        print(soma)
    elif op == 2:
        soma = n1 * n2
        print(soma)
    elif op == 3:
        if n1 > n2:
            print(f'The first selected number {n1} is bigger than the second selected number {n2}')
        else:
            print(f'The first selected number {n1} is less than the second selected number {n2}')
    elif op == 4:
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
        print(n1,  n2)
    elif op == 5:
        print('You left the program')
        end = 0
    sleep(3)
