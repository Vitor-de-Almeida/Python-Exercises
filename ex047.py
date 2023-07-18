"""Make a program that shows on the screen all pairs number between 1 and 50"""
count = 0
for c in range(0, 10, 1):
    if c % 2 == 0 and c != 0:
        count = count + 1
        print(c)
print(f'The numbers of pair number is {count}')
