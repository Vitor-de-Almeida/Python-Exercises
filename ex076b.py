"""Make a program that have a tuple with name of products and it respective prices.
At the end, show a list of prices organizing the data in table."""
var = ('Pencil', 0.30, 'Rubber', 0.20, 'Copybook', 3.75, 'Book', 9.00, 'Compass', 3.45,
       'Schoolbag', 12.00, 'Pen', 0.90, 'Soft pencil', 1.50)
print('-'*38)
print(f'\033[1;97m{"List of Prices":^35}\033[m')
print('-'*38)
for c in range(0, len(var)):
    if c % 2 == 0:
        print(f'{var[c]:.<30}', end='')
    else:
        print(f'${var[c]:>7.2f}')
print('-'*38)

