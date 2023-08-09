"""Make a program that have a tuple with name of products and it respective prices.
At the end, show a list of prices organizing the data in table."""
var = ('\033[1;34mPencil.......................................$  ', 0.30,
       'Rubber.......................................$  ', 0.20,
       'Copybook.....................................$  ', 3.75,
       'Book.........................................$  ', 9.00,
       'Compass......................................$  ', 3.45,
       'Schoolbag....................................$  ', 12.00,
       'Pen..........................................$  ', 0.90,
       'Soft pencil..................................$  ', 1.50, '\033[m')
print('-'*40)
print('\033[1;97mList of Prices\033[m')
print('-'*40)
for c in range(0, len(var)-1, 2):
    print(var[c], var[c+1])
print('-'*40)









