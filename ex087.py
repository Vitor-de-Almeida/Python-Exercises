"""Improve the previous challenge, showing at the end:
a) The sum of all even values entered.
b) The sum of the values in the third column.
c) The largest value in the second row."""
matriz = [[0.0, 0.1, 0.2], [1.0, 1.1, 1.2], [2.0, 2.1, 2.2]]
pair = 0
soma = 0
bn = 0
for c in range(0, 3):
    for p in range(0, 3):
        matriz[c][p] = int((input(f'Enter an value for [{c}, {p}]: ')))
print('-=-'*10)
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[c][p]:^5}]', end='')
        if matriz[c][p] % 2 == 0:
            pair = pair + matriz[c][p]
        if p == 0:
            bn = matriz[1][p]
        elif matriz[1][p] > bn:
            bn = matriz[1][p]
    soma = soma + matriz[c][2]
    print('')
print('-=-'*10)
print(f'The sum of pair values are {pair}')
print(f'The sum of values of third colum are {soma}')
print(f'The biggest value of the second line is {bn}')
