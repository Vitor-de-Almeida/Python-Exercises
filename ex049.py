#Write a program that reads any integer and displays its table on the screen.
n1 = int(input('Write a number to see its table: '))
print('\033[1;33m-\033[m'*11)
for c in range(0, 11):
    print(f'\033[1;34m{n1} x {c:2} = {n1 * c}\033[m')
print('\033[1;33m-\033[m'*11)
