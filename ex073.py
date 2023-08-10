"""Create a tuple filled with the top 20 of the Brazilian Football Championship Table, in order of placement.
Then show:
a) Only the top 5 finishers.
b) The last 4 placed in the table.
c) A list of teams in alphabetical order.
d) In which position in the table is the "Coritiba" team."""
tp = ('Botafogo', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense', 'Athletico-PR', 'Bragantino', 'São Paulo',
      'Cuiabá', 'Internacional', 'Cruzeiro', 'Fortaleza', 'Atlético-MG', 'Corinthians', 'Goiás', 'Santos', 'Bahia',
      'Coritiba', 'América-MG', 'Vasco da Gama')
print('\033[1;97m-=-\033[m'*20)
print('\033[1;97m-=-\033[m'*20)
print(f'\033[1;34mThe teams of brazilian football championship are:')
for c in range(0, 19):
    print(f'\033[1;34m{tp[c]}', end=', ')
print(f'\033[1;34m{tp[19]}.')
print('\033[1;97m-=-\033[m'*20)
print('\033[1;97m-=-\033[m'*20)
print(f'\033[1;97mThe top five of the brazilian football championship are:\033[m')
for top in tp[0:4]:
    print(f'\033[1;97m{top}\033[m', end=', ')
print(f'\033[1;97m{tp[4]}.\033[m')
print('\033[1;97m-=-\033[m'*20)
print('\033[1;97m-=-\033[m'*20)
print(f'\033[1;34mThe last four placed in the table of the brazilian football championship are:\033[m')
for f in range(-4, 0):
    print(f'\033[1;34m{tp[f]}\033[m', end=', ')
print(f'\033[1;34m{tp[19]}.\033[m')
print('\033[1;97m-=-\033[m'*20)
print('\033[1;97m-=-\033[m'*20)
print(f'\033[1;33mThe list of teams in alphabetical order of the brazilian football championship are:\033[m')
for d in sorted(tp):
    print(f'\033[1;33m{d}\033[m', end=', ')
print('\n', '\033[1;97m-=-\033[m'*20)
print('\033[1;97m-=-\033[m'*20)
print(f'\033[1;31m"Coritiba" team is in the position of {tp.index("Coritiba")+1}ª\033[m')
print('\033[1;97m-=-\033[m'*20)
print('\033[1;97m-=-\033[m'*20)


