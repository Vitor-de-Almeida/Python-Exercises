num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Five not found')
print(f'{num}')
print(f'This list has {len(num)} elements')



valor = list()
for cont in range(0,5):
    valor.append(int(input('Enter the number you want:')))
for c, v in enumerate(valor):
    print(f'In the position {c}, found {v}!')
print('Got at the end of the list.')



a= [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'List A:{a}')
print(f'List B:{b}')








