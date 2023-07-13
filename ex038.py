"""#Write a program that reads two integer and compare them displaying on the screen a message:
- The first number is the higher
- The second number is higher
- There is no higher integer, both are equal"""
n1 = int(input('\033[1;34mEnter the first integer:\033[m '))
n2 = int(input('\033[1;34mEnter the second integer:\033[m '))
if n1 > n2:
    print(f'The first number \033[1;32m{n1}\033[m is higher than the second \033[1;35m{n2}\033[m!')
elif n1 < n2:
    print(f'The second number \033[1;32m{n2}\033[m is higher than the first \033[1;35m{n1}\033[m!')
else:
    print(f'\033[1;34mThere is no higher number, both are equal!\033[m')
