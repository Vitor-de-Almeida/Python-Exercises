"""Make a program that reads a student's name and average, also saving the situation in a dictionary.
At the end, show the contents of the structure on the screen."""
boletim = dict()
print(f'{"-=-"}'*2, f'{"Welcome":^12}', f'{"-=-"}'*2)
boletim['Name'] = str(input('\033[1;32mEnter your name: \033[m')).strip()
boletim['Average'] = float(input(f'\033[1;32mAverage Scores of {boletim["Name"]}: \033[m'))
print(f'\033[1;97mThe name is {boletim["Name"]}\033[m')
print(f'\033[1;97mThe average score is {boletim["Average"]:.1f}\033[m')
if boletim["Average"] > 7:
    print('\033[1;34mThe student passed!\033[m')
else:
    print('\033[1;31mThe student failed!\033[m')


