"""Write a program that calculates the sum of all odd numbers that are multiples of three and are in the range 1 to 500"""
soma = 0
for c in range(1, 501, 2):
    if c % 2 == 1 and c % 3 == 0:
        soma = c + soma
print(f'The sum of all odd numbers that are multiples of three are: {soma}')
