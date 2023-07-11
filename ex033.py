"""#Make a program that reads three numbers and displays on the screen which of them are the higher and the lower"""
print('\033[4;36mEnter three numbers and the computer will tell you the higher and the lower between them.\033[m')
n1 = int(input('Enter the first number:'))
n2 = int(input('Enter the second number:'))
n3 = int(input('Enter the third number:'))
lower = n1
if n2 < n1 < n3:
    lower = n2
if n3 < n2 < n1:
    lower = n3
higher = n1
if n2 > n1 and n2 > n3:
    higher = n2
if n3 > n1 and n3 > n2:
    higher = n3
if n1 == n2 and n3 > n2:
    higher = n3
    lower = n2
if n1 == n2 and n3 < n2:
    higher = n2
    lower = n3
if n3 == n2 and n1 > n2:
    higher = n1
    lower = n2
if n3 == n2 and n1 < n2:
    higher = n3
    lower = n1
if n1 == n3 and n2 > n3:
    higher = n2
    lower = n3
if n1 == n3 and n2 < n3:
    higher = n1
    lower = n2
print(f'\033[1;33mThe higher number is {higher} and the lower number is {lower}\033[m')


