"""#Make a program that reads any year and shows if it is a leap year."""
from datetime import date
y = int(input("\033[1;34mEnter a year and I will tell you if it was or will be a leap year! \033[m"))
if y == 0:
    y = date.today().year
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(f'The entered year {y} is a leap year!')
else:
    print(f'The entered year {y} is not a leap year!')
