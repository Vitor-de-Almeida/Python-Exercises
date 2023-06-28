"""# Write a program that reads a sentence from the keyboard and displays:

-> How many times does the letter "a" appear.

-> In what position does it appear the first time.

-> In what position did it appear last time."""

r = str(input('Enter a random phrase: '))
print(r.count('a'))
print(r.find('a'))
print(r.find('a', 1))
