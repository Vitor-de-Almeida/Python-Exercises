"""Create a program that reads the name, year of birth and employment card and register them in a dictionary.
If the user has an employment card (employment card != 0),
the dictionary will also receive the year of hiring and the user's salary.
Calculate and add, in addition to age, with how many years the person will get the retirement,
considering that the working time is 35 years."""
from datetime import date
year = date.today().year
data = dict()
data['name'] = str(input('Name: '))
age = int(input('Year of birth: '))
data['age'] = year - age
data['employmentcard'] = int(input('Employment Card: (0 not have)'))
if data['employmentcard'] == 0:
    for k, v in data.items():
        print(f'{k} has the value {v}')
else:
    contdate = int(input('Year of hiring: '))
    data['hiring'] = contdate
    data['salary'] = float(input('Salary(payment): '))
    data['retirement'] = data['age'] + (35-(year-data['hiring']))
    print(data)
    for k, v in data.items():
        print(f'{k} has the value {v}')






