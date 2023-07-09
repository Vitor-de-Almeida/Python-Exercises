"""#Make a program that ask your employee his wage and calculate its increase.
To salaries superior to $ 5000 dollars, the increase is to 10%.
To salaries inferior or equal to $ 5000 dollars, the increase is to 15%. Show the results on the screen"""
s = int(input('Enter your current salary on the company:'))
if s > 5000:
    print(f'With the increase your new salary is:{(s*110)/100}')
else:
    print(f'With the increase your new salary is:{(s*115)/100}')

