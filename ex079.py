"""Create a program where the user can type several numeric values and register them in a list.
If the number already exists in there, it will not be added.
At the end, all unique values entered will be displayed, in ascending order."""
numbers = list()
c = 0
while True:
    numbers.append(int(input('\033[1;34mEnter an number: \033[m')))
    if numbers.count(numbers[c]) > 1:
        numbers.remove(numbers[c])
        print('\033[1;36mValue already added. Please try another!\033[m')
    else:
        print('\033[1;33mValue added successful\033[m')
        c += 1
    #c += 1
    cond = str(input('\033[1;97mDo you want to continue? [Y/N] \033[m')).strip().lower()
    if cond == 'n':
        break
print('=-='*5)
numbers.sort()
print(numbers)
print('=-='*4)



