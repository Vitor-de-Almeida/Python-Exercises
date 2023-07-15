"""#The national swimming confederation needs a program that reads the year of birth of an athlete
and shows his category, according to age:
- Up to 9 years old: Baby;
- Up to 14 years: Infant;
- up to 19 years old: Junior;
- Up to 20 years: Senior;
- Above: Master."""
birth = int(input('\033[1;34mWhat is the year you were born?\033[m '))
from datetime import date
today = date.today().year
age = today - birth
if age <= 9:
    print(f'\033[1;33mAccording to your age {age}, you fit the category Baby!\033[m')
elif 9 < age <= 14:
    print(f'\033[1;34mAccording to your age {age}, you fit the category Infant!\033[m')
elif 14 < age <= 19:
    print(f'\033[1;35mAccording to your age {age}, you fit the category Junior!\033[m')
elif 19 < age <= 20:
    print(f'\033[1;36mAccording to your age {age}, you fit the category Senior!\033[m')
else:
    print(f'\033[1;97mAccording to your age {age}, you fit the category Master!\033[m')
