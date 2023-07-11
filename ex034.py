"""#Make a program that ask your employee his wage and calculate its increase.
To salaries superior to $ 5000 dollars, the increase is to 10%.
To salaries inferior or equal to $ 5000 dollars, the increase is to 15%. Show the results on the screen"""
s = int(input('\033[4;31mEnter your current salary on the company:\033[m '))
if s > 5000:
    print(f'\033[1;32mWith the increase your new salary is: {(s*110)/100:.2f}\033[m')
else:
    print(f'\033[1;34mWith the increase your new salary is: {(s*115)/100:.2f}\033[m')

