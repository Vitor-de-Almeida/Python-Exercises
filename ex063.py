"""Write a program that reads any integer n and displays the first n elements of a fibonacci sequence on the screen"""
n = int(input('\033[1;34mEnter the position of a number to see the fibonacci sequence on the screen:\n\033[m'))
count = 3
n3 = 1
n1 = 0
n2 = 1
print(f'\033[4;30;107mThe {n2}º term of Fibonnaci sequence is {n1}\033[m')
print(f'\033[4;30;107mThe 2º term of Fibonnaci sequence is {n2}\033[m')
while count != (n+1):
    n3 = n2 + n1
    print(f'\033[4;30;107mThe {count}º term of Fibonnaci sequence is {n3}\033[m')
    n1 = n2
    n2 = n3
    count = count + 1
#print(f'\033[4;30;107mThe {count-1}º term of Fibonnaci sequence is {n3}!\033[m')
