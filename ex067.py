"""Write a program that displays the table of several numbers, one at a time, for each value entered by the user.
The program will stop when the requested number is negative."""
while True:
    n = int(input('\033[1;32mEnter any number you want to see the multiplication table: \033[m'))
    if n <= 0:
        break
    print(23*'-')
    for c in range(1, 11):
        print(f'\033[1;4;34m{n} x {c} = {n*c}\033[m')
    print(23 * '-')
print('\033[4;97;40mMultiplication Table closed. Check back when you want!\033[m')

