"""create a program that reads the year of birth of seven people. At the end, show how many people have not yet
reached the age of majority and how many are already of age"""
from datetime import date
today = date.today().year
old = 0
young = 0
for c in range(0, 7):
    year = int(input('\033[4;97;43mEnter the year you were born:\033[m '))
    age = today - year
    if age >= 21:
        old += 1
    else:
        young += 1
print(f'\033[4;36;40mThere are {old} adults and {young} teenagers\033[m')

