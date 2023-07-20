"""Develop a program that reads the name, age, and gender of four people.
At the end of the program, show on the screen:
1 - The average of age between them
2 - Who is the older
3 - How many women has less than 20 years"""
cage = 0
fem = 0
age2 = 0
qt = 0
name2 = ''
gender = ''
gender2 = ''
for p in range(1, 5):
    name = str(input(f'Enter the name of {p}ª person: ')).strip()
    age = int(input(f'Enter the age of {p}ª person: '))
    gender = str(input(f'Enter the gender of {p}ª person, [M/F]: ')).strip().lower()
    cage += age
    if gender in 'm' and age > age2:
        name2 = name
        age2 = age
        gender2 = gender
    elif gender in 'f' and age < 20:
        fem += 1
    qt = p
average = (cage/qt) #def media

print(f'The average age of the group is {average}')
if gender2 == 'm':
    print(f'The older man is {name2} and his age is {age2}')
else:
    print('There are no men in this selection')
if fem == 1:
    print(f'There is {fem} under twenty years in this selection')
if fem > 1:
    print(f'There are {fem} under twenty years in this selection')
