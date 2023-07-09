"""#Make a program that reads three numbers and displays on the screen which of them are the higher and the lower"""
print('Enter three numbers and the computer will tell you the higher and the lower between them.')
n1 = int(input('Enter the first number:'))
n2 = int(input('Enter the second number:'))
n3 = int(input('Enter the third number:'))
if n1 > n2 and n1 > n3:
    print(f'The higher number is {n1}')
if n2 > n1 and n2 > n3:
    print(f'The higher number is {n2}')
if n3 > n1 and n3 > n2:
    print(f'The higher number is {n3}')
if n1 < n2 and n1 < n3:
    print(f'The lower number is {n1}')
if n2 < n1 and n2 < n3:
    print(f'The lower number is {n2}')
if n3 < n1 and n3 < n2:
    print(f'The lower number is {n3}')
