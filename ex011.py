#make a program that reads the width and height of a wall in meters,
#calculates its area and the amount of paint needed to paint it,
#knowing that each liter of paint paints an area of 2 m².
w = float(input('Enter the width: '))
h = float(input('Enter the height: '))
a = (w*h)
print(f' The wall has {a} m² and the amount of liters you need to paint this wall is {a/2} l of ink!')
