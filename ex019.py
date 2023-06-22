"""#A professor wants to draw one of his four students to erase the board. Make a program that helps him, reading their
name and writing the name of the chosen one."""
from random import choice
n1 = str(input('Enter the name of one student: '))
n2 = str(input('Enter the name of one student: '))
n3 = str(input('Enter the name of one student: '))
n4 = str(input('Enter the name of one student: '))
students = [n1, n2, n3, n4]
chosen = choice(students)
print(f'The student drawn to erase the board was: {chosen}')


