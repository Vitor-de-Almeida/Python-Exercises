"""Write a program that has a function called greater(), which takes several parameters with integer values.
Your program has to analyze all the values and say which one is the largest."""


def bigger(*num):
    big = 0
    print('-=-'*7)
    print('\033[1;97manalyzing past values\033[m')
    for c in range(0, len(num)):
        print(f'\033[1;36m{num[c]}\033[m', end=' ')
        if c == 0:
            big = num[c]
        else:
            if num[c] > big:
                big = num[c]
    print(f'\033[1;36m. {len(num)} values were reported in total!\033[m')
    print(f'\033[1;34mThe highest value reported was {big}\033[m')
    print('-=-'*7)


bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger(0)

