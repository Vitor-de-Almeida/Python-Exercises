"""Make a program that reads integers. The program will only stop when the user wants to stop.
After the break, the program must show on the screen the average of all values
and which was the highest and lowest of the values read"""
n = 0
count = 0
sm = 0
c = ''
b = 0
p = 0
while c != 'n':
    n = int(input('\033[1;34mEnter an integer:\n\033[m'))
    c = str(input('\033[1;33mYou want to continue [Y/N]:\n\033[m'))
    count += 1
    sm = sm + n
    if count == 1:
        b = n
        p = n
    else:
        if n > b:
            b = n
        if n < p:
            p = n

print(f'\033[4;97mThere was {count} integers written and the average between them is {sm/count}!'
      f'\nThe greatest integer was {b} and the lowest was {p}!\033[m')