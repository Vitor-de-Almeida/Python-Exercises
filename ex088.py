"""Write a program that helps a lottery player make guesses.
The program will ask how many games will be generated and will raffle 6 numbers between 1 and 60 for each game,
registering everything in a composite list"""
from random import sample
from time import sleep
cont = 0
print('_'*30)
print(f'{"-=-Lottery-=-":^30}')
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
    sleep(0.8)
print(f'{"Good Luck!":^30}')

