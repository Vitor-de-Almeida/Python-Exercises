"""#make a program that reads a person's full name and displays on the screen the first and the last name separately"""
n = str(input('Enter your full name: ')).strip()
print('Pleasure to meet you!')
print('Your first name is:', (n.split()[0]))
print(f'Your last name is: {(n.split()[-1])}')

