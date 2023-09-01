"""Make a program that has a function called area(), which receives the dimensions of a rectangular
terrain (width and length) and shows the area of the terrain."""


def area(w, lt):
    a = w*lt
    print(f'The area of a property {w}m x {lt}m is equal to {a}m².')


print('-'*17)
print('Property Controls')
print('-'*17)
w = float(input('Width (m): '))
lt = float(input('Length (m): '))
area(w, lt)







