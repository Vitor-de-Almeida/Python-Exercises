"""Create a program where 4 players roll a die and get random results.
Store these results in a dictionary.
In the end, put that dictionary in order, knowing that the winner got the highest number on the dice."""
from random import randint
count = 1
print(f'{"=-="}'*4, f'{"Welcome to the Game":^5}', f'{"=-="}'*4)
game = dict()
players = []
for c in range(0, 4):
    game['Player'] = f'Player {c+1}'
    game['Result'] = randint(1, 6)
    players.append(game.copy())
print(f'{"=-="}'*4, f'{"Sorted Values":^5}', f'{"=-="}'*4)
for c in range(0, 4):
    print(f'The {players[c]["Player"]} has {players[c]["Result"]}')
print(f'{"=-="}'*4, f'{"Players Ranking":^5}', f'{"=-="}'*4)
print(players)
for p in players:
    #for v in p.keys():
        #print(f'{count}º place: The {v} got')
    #count += 1
    print(f'{count}º place: The {p["Player"]} got {p["Result"]}')
    count += 1



