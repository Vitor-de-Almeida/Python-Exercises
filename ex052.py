"""write a program that reads an integer and tells whether it is a prime number."""
n = int(input('Enter a integer: '))
s = 0
count = 0
for c in range(1, 11):
    s += 1
    if n % s == 0:
        count += + 1
        print(f'\033[1;34m{s} \033[m')
    else:
        print(f'\033[1;31m{s} \033[m')
if count <= 2:
    print(f'The number {n} was divisible {count} times. For this, he is a prime number')
else:
    print(f'The number {n} was divisible {count} times. For this, he is not a prime number')
