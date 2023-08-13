"""Make a program that reads several numbers and put them into a list.
After that, show on the screen:
a)How many numbers where digited;
b)The list of values, ordered in descending order;
c)If 5 were digited in the list"""
numbers = list()
cont2 = 0
while True:
    numbers.append(int(input('Enter an number: ')))
    cont = str(input('Do you want to continue? [Y/N]')).strip().lower()
    cont2 += 1
    if cont == 'n':
        break
numbers.sort(reverse=True)
five = numbers.count(5)
print('-=-'*10)
print(f'{cont2} elements were typed')
print('-=-'*10)
print(f'The values entered in descending order are {numbers}')
print('-=-'*10)
if five >= 1:
    print(f'The value 5 make part of the list')
else:
    print(f"The value 5 didn't make part of the list")
print('-=-'*10)
