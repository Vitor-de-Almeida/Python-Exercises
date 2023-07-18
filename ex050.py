"""Write a program that reads six integers and calculates the sum of all pairs of numbers"""
soma = 0
for c in range(1, 7):
    n = int(input('Enter an integer number: '))
    if n % 2 == 0:
        soma = n + soma
print(f'The sum of all pairs and integers are: {soma}')
