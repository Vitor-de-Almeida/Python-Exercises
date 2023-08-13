"""Create a program where the user can type five numeric values and register them in a list, on the right position.
You can not use sort(). At the end, show on the screen the ordered list."""
numbers = list()
nb = nl = 0
for c in range(0, 5):
    num = int(input('enter a number: '))
    if c == 0 or num > numbers[-1]:
        numbers.append(num)
        print('Number added to the end of the list')
    else:
        pos = 0
        while pos <= len(numbers):
            if num <= numbers[pos]:
                numbers.insert(pos, num)
                print(f'Number added to the {pos} position of the list')
                break
            pos += 1
print(numbers)


