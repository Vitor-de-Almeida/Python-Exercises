"""Make a program that reads the age and the gender of many people.
For every people registered, the program must ask the user if he wants to continue or not. At the end, show on the screen:
a - how many people has more than 18 years old.
b - how many men were registered.
c - how many women have less than 20 years old.
"""
totaladult = 0
totalman = 0
totalwoman = 0
while True:
    print('\033[1;37m-\033[m'*17)
    print('\033[1;97mRegister a person\033[m')
    print('\033[1;37m-\033[m' * 17)
    age = int(input('\033[1;97mAge: \033[m'))
    gender = str(input('\033[1;97mGender[M/F]: \033[m')).strip().lower()[0]
    while gender not in 'm' and gender not in 'f':
        gender = str(input('\033[1;97mGender[M/F]: \033[m')).strip().lower()[0]
    if age > 18:
        totaladult += 1
    if gender == 'm':
        totalman += 1
    if gender == 'f' and age < 20:
        totalwoman += 1
    print('\033[1;37m-\033[m' * 17)
    cont = str(input('\033[1;97mDo you want to continue?[Y/N]: \033[m')).strip().lower()[0]
    while cont not in 'y' and cont not in 'n':
        cont = str(input('\033[1;97mDo you want to continue?[Y/N]: \033[m')).strip().lower()[0]
    if cont == 'n':
        break
print(15*'\033[1;34m=\033[m', '\033[1;34mEnd of the Program\033[m', 15*'\033[1;34m=\033[m')
print(f'\033[1;37mTotal of person with more than 18 years old: {totaladult}\033[m')
if totalman == 1:
    print(f'\033[1;34mIn all we have {totalman} man registered\033[m')
else:
    print(f'\033[1;34mIn all we have {totalman} men registered\033[m')
if totalwoman == 1:
    print(f'\033[1;34mIn all we have {totalwoman} woman with less than 20 years old\033[m')
else:
    print(f'\033[1;34mIn all we have {totalwoman} women with less than 20 years old\033[m')
print(15*'\033[1;37m=\033[m', '\033[1;34mEnd of the Program\033[m', 15*'\033[1;34m=\033[m')






