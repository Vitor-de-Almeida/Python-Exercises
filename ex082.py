"""Make a program that reads several types of numbers and put them into a list.
After that, create another two extras list, which one must content only odd and another even numbers.
At the end, show the content of the three lists"""
numbers = list()
numbers2 = list()
numbers3 = list()
count2 = 0
while True:
    numbers.append(int(input('Enter an number: ')))
    cont = str(input('Do you want to continue? [Y/N]')).strip().lower()
    if cont == 'n':
        break
for c in range(0, len(numbers)):
    if numbers[c] % 2 == 0:
        numbers2.append(numbers[c])
    else:
        numbers3.append(numbers[c])
print('-=-'*14)
print(f'The complete list is {numbers}')
print(f'The complete pair list is {numbers2}')
print(f'The complete odd list is {numbers3}')
print('-=-'*14)

