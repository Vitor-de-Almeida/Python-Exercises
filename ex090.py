"""Make a program that reads a student's name and average, also saving the situation in a dictionary.
At the end, show the contents of the structure on the screen."""
boletim = dict()
print(f'{"-=-"}'*2, f'{"Welcome":^12}', f'{"-=-"}'*2)
boletim['Name'] = str(input('\033[1;32mEnter your name: \033[m')).strip()
boletim['Average'] = float(input(f'\033[1;32mAverage Scores of {boletim["Name"]}: \033[m'))
if boletim["Average"] >= 7:
    boletim['Situation'] = 'Approved'
elif 5 <= boletim["Average"] < 7:
    boletim['Situation'] = 'exam'
else:
    boletim['Situation'] = 'Failed'
for k, v in boletim.items():
    print(f'\033[1;34m- {k} is equal to {v}')

