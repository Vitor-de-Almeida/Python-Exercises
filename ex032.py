"""#Make a program that reads any year and shows if it is a leap year."""
y = int(input("Enter a year and I will tell you if it was or will be a leap year!"))
if y % 4 == 0:
    print('The entered year is a leap year!')
else:
    print('The entered year is not a leap year!')
