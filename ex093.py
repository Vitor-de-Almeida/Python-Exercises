"""

"""
score = dict()
numberofgoals = list()
cont = 0
score['name'] = str(input('\033[1;34mName of the player: \033[m'))
matches = int(input(f'\033[1;32mHow many games did {score["name"]} played?: \033[m'))
for c in range(1, matches+1):
    numberofgoals.append(int(input(f'\033[1;36mHow many goals did {score["name"]} score in the match {c}?\033[m')))
    cont += numberofgoals[c-1]
score['goals'] = numberofgoals
score['total'] = cont
print('-=-'*18)
print(score)
print('-=-'*18)
for k, v in score.items():
    print(f'\033[1;97;40mThe field {k} has the value {v}.\033[m')
print('-=-'*18)
print(f'\033[1;34mThe player {score["name"]} played {matches} matches!\033[m')
for c in range(0, len(numberofgoals)):
    print(f'\033[1;35mIn the match {c+1}, he did {numberofgoals[c]} goals!\033[m')

