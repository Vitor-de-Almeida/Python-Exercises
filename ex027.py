#make a program thats reads a person's full name and displays on the screen the first and the last name separately
n = (input('Enter your full name: '))
print('Your first name is:', (n.split()[0]))
print('Your last name is:', (n.rsplit()[-1]))




