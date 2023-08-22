"""Create a program that reads the name and two grades of several students and stores them in a composite list.
At the end, it shows a bulletin containing the average of each one and
allows the user to show the grades of each student individually.
"""
boletimstudent = []
n = 0
while True:
    name = (str(input('\033[1;34mName: \033[m')))
    n1 = float(input('\033[1;34mScore1: \033[m'))
    n2 = float(input('\033[1;34mScore2: \033[m'))
    calc = (n1 + n2)/2
    boletimstudent.append([name, n1, n2, calc])
    cont = str(input('\033[1;36mDo you want to continue ? [Y/N]\033[m')).strip().lower()
    if cont == 'n':
        break
print('\033[1;35m-='*30)
print(f'{"Number":<7}{"Name":<10}{"Average":>8}')
for pos, p in enumerate(boletimstudent):
    print(f'{pos+1:<7}{p[0]:<10}{p[3]:>8.2f}')
while n != 999:
    n = int(input('What student you want to see the scores?'))
    if n == 999:
        break
    print(f'The scores of {boletimstudent[n-1][0]} are {boletimstudent[n-1][1]} and {boletimstudent[n-1][2]}')











