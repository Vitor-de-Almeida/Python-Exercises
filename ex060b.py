"""Make a program that reads any number and show on the screen the factorial of it"""
n = int(input("\033[1;97mEnter any number you want to calculate it's factorial: \033[m"))
count = n
while n != 1:
    print(n)
    count = count*(n-1)
    n = n-1
print(f'\033[1;34mThe factorial of {n}! is {count:.1f}\033[m')
