"""Create a program where the user can enter seven numeric values and register them in a single list that
keeps even and odd values separate.
At the end, show the even and odd values in ascending order."""
numbers = list()
pair = list()
odd = list()
numbers.append(pair[:])
numbers.append(odd[:])
print(numbers)
for c in range(0, 7):
    n = int(input(f'Enter the {c+1}º number: '))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)
print(f'The pairs values entered were: {sorted(numbers[0])}')
print(f'The odd values entered were: {sorted(numbers[1])}')

