"""#Create a program that reads two grades from a student and calculates their average,
showing a message at the end, according to the average achieved:
- Average below 5.0: failed
- Average between 5.0 and 6.9: recovery
- Average 7.0 or above: approved"""
n1 = float(input('\033[1;32mEnter your grade on the first exam:\033[m '))
n2 = float(input('\033[1;32mEnter your grade on the second exam:\033[m '))
med = (n1 + n2)/2
if med < 5.0:
    print(f'\033[1;31mYour note is {med:.1f} !. You failed! You must study much more or you will repeat the school '
          f'year!\033[m')
elif 5.0 <= med <= 6.99:
    print(f'\033[1;33mYour note is {med:.1f} !. You stayed recovery! You must study a little bit more\033[m')
elif med >= 7.0:
    print(f'\033[1;34mYour note is {med:.1f} !. You passed the year! Congratulations!!\033[m')
