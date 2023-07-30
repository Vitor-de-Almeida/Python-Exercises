"""Make a program that reads many integers. The program will only stop when the user enter '999', which is
the stop condition. At the end, show on the screen how many integers were entered and what is the sum between them"""
count = soma = 0
while True:
    n = int(input('\033[1;34mEnter an integer(999 to stop):\n \033[m'))
    if n == 999:
        break
    count += 1
    soma += n
print(f'\033[1;97m{count} numbers have been entered and the sum between them are {soma}\033[m')

