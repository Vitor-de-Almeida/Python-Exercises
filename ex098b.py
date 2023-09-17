"""Make a program that has a function called counter(), which receives three parameters:
start, end and step and performs the count.
Your program has to perform three counts through the created function:
a) From 1 to 10, from 1 to 1
b) From 10 to 0, from 2 to 2
c) A custom count"""

def counter(beg, end, step):
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


print('-=-'*7)
print(f'Counter from 1 until 10 from 1 to 1')
counter(1, 10, 1)
print(f'Counter from 10 until 0 from 2 to 2')
counter(10, 0, 1)

print('Now is your turn to custom the counter!')
print('-=-' * 13)
beg = int(input('Start:'))
e = int(input('End:'))
s = int(input('Step:'))
print('-=-' * 13)
print(f'Counter from {beg} until {e} from {s} to {s}')
print('-=-' * 13)
counter(beg, e, s)

