"""#Write a program that reads the birth of a young person and informs according to his age:
 - If he is still going to enlist in the military
 - If it is time to enlist in the military
 - If it is past the enlistment time"""
birth = int(input('\033[1;31mEnter the year you were born?:\033[m '))
from datetime import date
today = date.today().year
age = today - birth
dif = 18 - age
difold = age - 18
if age < 18:
    print(f"\033[1;97mWho was born in {birth} have {age} years old in {today}.\033[m")
    print(f'\033[1;97m{dif} years left for the enlistment. Your enlistment will be in {today+dif}\033[m')
elif age == 18:
    print(f'\033[1;36mYou have {age} years old now. You have the correct age to enlist in {today}. Welcome to the '
          f'military service.\033[m')
else:
    print(f"\033[1;97mWho was born in {birth} have {age} years old in {today}.\033[m")
    print(f'\033[1;97mYou passed {difold} years for the enlistment. Your enlistment should have been done in {today - difold}\033[m')
