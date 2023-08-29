"""Create a program that reads the name, gender and age of several people,
storing each person's data in a dictionary and all dictionaries in a list.
At the end, show:
a) How many people were registered.
b) The average age of the group.
c) A list of all women.
d) A list of all people above average age."""
print('-=-'*10)
print(f'\033[1;34m{"Welcome":^27}\033[m')
print('-=-'*10)
category = dict()
people = list()
countw = 0
som = 0
while True:
    category['name'] = str(input('Name: '))
    while True:
        category['gender'] = str(input('Gender: ')).strip().lower()
        if category['gender'] == 'f':
            countw += 1
        if category['gender'] in 'm' or category['gender'] in 'f':
            break
        print('Error! Please, enter your correct gender!')
    category['age'] = int(input('Age: '))
    while True:
        n = str(input('Do you want to continue? [Y/N]')).strip().lower()
        if n in 'yn':
            break
    people.append(category.copy())
    if n == 'n':
        break
print('-=-'*16)
print(f'\033[1;36mThe group has {len(people)} people!\033[m')
for c in range(0, len(people)):
    som = som + people[c]["age"]
med = som/len(people)
print(f'\033[1;36mThe average age of group is {med:5.1f} years!\033[m')
if countw == 1:
    print(f'\033[1;36mThe woman registered is:\033[m', end=' ')
elif countw >= 1:
    print(f'\033[1;36mThe women registered are:\033[m', end=' ')
else:
    print(f'\033[1;36mThere is no woman registered! \033[m', end=' ')
for c in range(0, len(people)):
    if people[c]['gender'] == 'f':
        print(f'\033[1;36m{people[c]["name"]}\033[m', end=' ')
print()
print('-=-'*16)
print('\033[1;34mList of the people above the average age!\033[m')
print()
for c in range(0, len(people)):
    if people[c]['age'] > med:
        print(f'Name = {people[c]["name"]}; Gender = {people[c]["gender"].upper()}; Age = {people[c]["age"]};')
        print()


