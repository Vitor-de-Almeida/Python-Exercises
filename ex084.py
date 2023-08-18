"""Make a program that reads the name and the weight of random people and put it into a list.
At the end, show on the screen:
a) How many people were registered;
b) A list with the heaviest people;
c) A list with the lightest people."""
data = list()
people = list()
bw = lw = 0
while True:
    data.append(str(input('\033[1;34mEnter your name: \033[m')).strip())
    data.append(float(input('\033[1;34mEnter your weight: \033[m')))
    people.append(data[:])
    data.clear()
    goon = input('\033[1;34mDo you want to continue [Y/N]: \033[m').strip().lower()
    if goon[0] == 'n':
        break
print('-=-'*10)
print(f'\033[1;36mAt all, you registered {len(people)} people.')
for c in range(0, len(people)):
    if c == 0:
        bw = lw = people[0][1]
    else:
        if bw < people[c][1]:
            bw = people[c][1]
        if lw > people[c][1]:
            lw = people[c][1]
print(f'The highest weight was {bw} kg. It was the weights of', end=' ')
for pos in people:
    if pos[1] == bw:
        print(f'{pos[0]}', end=' ')
print(f'\nThe smallest weight was {lw} kg. It was the weights of', end=' ')
for pos2 in people:
    if pos2[1] == lw:
        print(f'{pos2[0]}', end=' ')



