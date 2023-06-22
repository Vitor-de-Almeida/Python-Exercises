"""#Write a program that reads the length of the opposite and adjacent sides of a right triangle.
#Calculate and show the length of the hypotenuse."""
o = float(input('Enter the length of the opposite side of the triangle: '))
a = float(input('Enter the length of the adjacent side of the triagle:'))
"""#First way to solve it!"""
hyp = (o**2+a**2)**(1/2)
print(f'The length of the hypotenuse is: {hyp:.2f}')
"""#second way to solve it!"""
print(f'The length of the hypotenuse is: {(o**2+a**2)**(1/2):.2f}')
"""#third way to solve it!"""
from math import hypot
print(f'The length of the hypotenuse is: {hypot(o,a):.2f}')