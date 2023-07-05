#make a program that reads a number from 0 to 9999 and displays each of the separate numbers on the screen
n = int(input('Enter a number between 0 and 9999:'))
u = n // 1 % 10
t = n // 10 % 10
h = n // 100 % 10
th = n // 1000 % 10
print(f'unit: {u}')
print(f'ten: {t}')
print(f'hundred: {h}')
print(f'thousand: {th}')



