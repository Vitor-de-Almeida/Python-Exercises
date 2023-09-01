"""Make a program that has a function called counter(), which receives three parameters:
start, end and step and performs the count.
Your program has to perform three counts through the created function:
a) From 1 to 10, from 1 to 1
b) From 10 to 0, from 2 to 2
c) A custom count"""


def counter(a, b):
    print('-=-'*7)
    for c in range(a, b+1):
        print(c, end=' ')
    print('END!')
    print('-=-' * 7)


def counter2(a, b):
    print('-=-'*7)
    for c in range(a, b, -2):
        print(c, end=' ')
    print('END!')
    print('-=-' * 7)


print('-=-'*7)
print(f'Counter from 1 until 10 from 1 to 1')
counter(1, 10)
print(f'Counter from 10 until 0 from 2 to 2')
counter2(10, 0)


def custom(beg, e, s):
    print('-=-' * 14)
    for c in range(beg, e, s):
        print(c, end=' ')
    print('END!')
    print('-=-' * 14)


print('Now is your turn to custom the counter!')
print('-=-' * 14)
beg = int(input('Start:'))
e = int(input('End:'))
s = int(input('Step:'))
print('-=-' * 14)
print(f'Counter from {beg} until {e} from {s} to {s}')
custom(beg, e, s)










