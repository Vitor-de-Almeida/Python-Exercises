"""Make a program that reads integers. The program will only stop when the user enter '999', which is
the stop condition. After the break, show how many number where entered and what is the sum between them"""
count = 0
sm = 0
n = int(input('\033[1;34mEnter an integer:\n\033[m'))
while n != 999:
    count += 1
    sm = sm + n
    n = int(input('\033[1;34mEnter an integer:\n\033[m'))
print(f'\033[4;97mThere was {count} integers written and the sum is {sm}!\033[m')



