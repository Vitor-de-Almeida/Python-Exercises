"""Make a program that has a list of called numbers and two functions called sortar() and sumpar().
The first function will classify 5 numbers and place them in the list and the second function
 will show the sum of all even values drawn by the previous function."""
from random import randint


def sort(lst):
    print("Sorting the five numbers of the list: ", end='')
    for c in range(0, 5):
        lst.append(randint(1, 10))
        print(f'{lst[c]}', end=' ')
    print()


def sumpair(lst):
    som = 0
    for p in lst:
        if p % 2 == 0:
            som += p
    print(f'Adding the even values of {numbers}, we got {som}')


numbers = list()
sort(numbers)
sumpair(numbers)


