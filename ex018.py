#make a program that reads any angle and shows on the screen the value of sine, cosine and tangent of that angle.
from math import radians, sin, cos, tan
ang = float(input('Enter an angle to read its sine, cosine and tangent:'))
sine = sin(radians(ang))
cosine = cos(radians(ang))
tangent = tan(radians(ang))
print(f'The entered angle has a sine,cosine and tangent equivalents to: Sin, {sine:.2f}, Cosine, {cosine:.2f}, Tangent, {tangent:.2f}')
