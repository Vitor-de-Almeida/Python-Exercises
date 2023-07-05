"""# Write a program that reads a sentence from the keyboard and displays:

-> How many times does the letter "a" appear.

-> In what position does it appear the first time.

-> In what position did it appear last time."""

r = str(input('Enter a random phrase: ')).strip()
r = r.replace('á', 'a')
r = r.replace('Á', 'A')
r = r.replace('À', 'A')
r = r.replace('à', 'a')
print(r.upper().count('A'))
print(r.upper().find('A')+1)
print(r.upper().rfind('A')+1)




