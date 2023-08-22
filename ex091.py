"""Create a program where 4 players roll a die and get random results.
Store these results in a dictionary.
In the end, put that dictionary in order, knowing that the winner got the highest number on the dice."""
from random import randint
from time import sleep
from operator import itemgetter
print(f'{"=-="}'*4, f'{"Welcome to the Game":^5}', f'{"=-="}'*4)
game = {'Player 1': randint(1, 6),
        'Player 2': randint(1, 6),
        'Player 3': randint(1, 6),
        'Player 4': randint(1, 6)}
ranking = dict()
print(f'{"=-="}'*4, f'{"Sorted Values":^5}', f'{"=-="}'*4)
for k, v in game.items():
    print(f'The {k} rolled a {v} on the dice!')
    sleep(0.4)
print(f'{"=-="}'*4, f'{"Players Ranking":^5}', f'{"=-="}'*4)
game = sorted(game.items(), key=itemgetter(1), reverse=True)
for c in range(0, 4):
    print(f'{c+1}º place: {game[c][0]} rolled a {game[c][1]} on the dice!')
    sleep(0.4)






