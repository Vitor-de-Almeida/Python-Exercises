"""#Create a program that reads an integer and show on the screen whether it is even or odd"""
n = int(input("\033[1;36mWhite an integer:\033[m"))
if n % 2 == 0:
    print(f'\033[1;33mThe number {n} is even!\033[m')
else:
    print(f'\033[1;35mThe number {n} is odd!\033[m')