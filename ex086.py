matriz = [[0.0, 0.1, 0.2], [1.0, 1.1, 1.2], [2.0, 2.1, 2.2]]
for c in range(0, 3):
    for p in range(0, 3):
        matriz[c][p] = int((input(f'Enter an value for [{c}, {p}]: ')))
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[c][p]:^5}]', end='')
    print('')


