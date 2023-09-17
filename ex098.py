"""Make a program that has a function called counter(), which receives three parameters:
start, end and step and performs the count.
Your program has to perform three counts through the created function:
a) From 1 to 10, from 1 to 1
b) From 10 to 0, from 2 to 2
c) A custom count"""


def counter(beg, end, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print('-=-' * 12)
    print(f'Counter from {beg} until {end} from {step} to {step}')
    print('-=-' * 12)
    if beg < end:
        #print('-=-' * 13)
        for c in range(beg, end+step, step):
            print(c, end=' ')
        print('END!')
        #print('-=-' * 13)
    else:
        #print('-=-' * 13)
        for c in range(beg, end-step, -step):
            print(c, end=' ')
        print('END!')
        #print('-=-' * 13)


counter(1, 10, 1)
counter(10, 0, 2)
print('-=-' * 13)
print('Now is your turn to custom the counter!')
print('-=-' * 13)
beg = int(input('Start:'))
e = int(input('End:'))
s = int(input('Step:'))
counter(beg, e, s)

