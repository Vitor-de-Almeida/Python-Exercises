from random import sample
cont = 0
print('_'*30)
print(f'{"Lottery":^30}')
print('_'*30)
n = int(input('\033[1;34mHow many games do you want me to draw? \n\033[m'))
card = list()
numbers = []
for d in range(1, 61):
    numbers.append(d)
while cont < n:
    card.append(sample(numbers, 6))
    cont += 1
print(f'{"Drawing Games":^30}')
for pos, p in enumerate(card):
    print(f'Game {pos+1}: {sorted(p)}')
print(f'{"Good Luck!":^30}')

