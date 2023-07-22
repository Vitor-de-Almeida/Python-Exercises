"""write a program that reads an integer and tells whether it is a prime number."""
n = int(input('Enter a integer: '))
count = 0
for c in range(1, n + 1):
    if n % c == 0:
        count += + 1
        print(f'\033[1;34m{c}\033[m', end=' ')
    else:
        print(f'\033[1;31m{c}\033[m', end=' ')
if count == 2:
    print(f'\n\033[1;97mThe number {n} was divisible {count} times.\nFor this, he is a prime number\033[m')
else:
    print(f'\n\033[4;97mThe number {n} was divisible {count} times.\nFor this, he is not a prime number\033[m')
