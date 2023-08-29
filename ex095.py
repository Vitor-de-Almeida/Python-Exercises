"""

"""
score = dict()
numberofgoals = list()
players = list()
while True:
    score['name'] = str(input('\033[1;34mName of the player: \033[m'))
    matches = int(input(f'\033[1;32mHow many games did {score["name"]} played?: \033[m'))

    for c in range(1, matches+1):
        numberofgoals.append(int(input(f'\033[1;36mHow many goals did {score["name"]} score in the match {c}?\033[m')))

    score['goals'] = numberofgoals[:]
    score['total'] = sum(numberofgoals)
    numberofgoals.clear()
    players.append(score.copy())

    ans = str(input('\033[1;36mDo you want to continue? [Y/N]')).strip().lower()
    if ans == 'n':
        break

print('-=-'*18)
print(players)
print('-=-'*18)
print(f'{"Position":<10}{"Name":<15}{"Goals":<15}{"Total":<15}')
print('-'*50)
#for p, player in enumerate(players):
    #print(f'{p+1:<7}{player["name"]:<18}{str(player["goals"]):<28}{player["total"]:<40}')
for p in range(0, len(players)):
    print(f'{p+1:<10}{players[p]["name"]:<15}{str(players[p]["goals"]):<15}{players[p]["total"]:<15}')
print('-'*40)
print('-=-'*18)
while True:
    w = int(input('What player you want to see the performance? (999 to exit)'))
    if w == 999:
        break
    if w > len(players) or w < 1:
        print(f'Error. There is no player with the code {w}. Try again!')
    else:
        print(f'--', f'RESULTS OF PLAYER {players[w-1]["name"].upper()}', '--')
        for k, v in enumerate(players[w-1]["goals"]):
            print(f'At the {k+1} game he/she did {v} goals!')
        #for p in range(0, len(players[w-1]["goals"])):
            #print(f'\033[1;36mAt the {p + 1} game he/she did {players[w-1]["goals"][p]} goals\033[m!')
print('-=-'*18)

