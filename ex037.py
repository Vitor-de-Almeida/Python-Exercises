"""Write a program that reads any integer and asks the user to choose the conversion base:
- 1 for binary
- 2 for octal
- 3 for hexadecimal"""
print('\033[1;32mWelcome to the base converter!\033[m')
n = int(input('\033[4;34m Write an integer you want to pick up:\033[m '))
op = int(input(('\033[1;34mThis are the options you must choose one:'
                '\n- 1 for binary \n- 2 for octal \n- 3 for hexadecimal\n')))
if op == 1:
    print(f'In binary base, the entered number is equivalent to {bin(n)[2:]}')
elif op == 2:
    print(f'In octal base, the entered number is equivalent to {oct(n)[2:]}')
elif op == 3:
    print(f'In hexadecimal base, the entered number is equivalent to {hex(n)[2:]}')

