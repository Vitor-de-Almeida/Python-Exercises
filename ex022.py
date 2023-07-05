"""#create a program that reads a persons full name and displays it on the screen!"""
name = str(input('Enter your full name, please: ')).strip()
print(f'Your name into uppercase letters is written this way: {name.upper()}')
print(f'Your name into lower case letters is written this way: {name.lower()}')
print(f'Your name length without space has {len(name.replace(" ", ""))} letters')
print('Your name length without space has {} letters'.format(len(name) - name.count(' ')))
print(f'The length of your fist name has {len(name.split()[0])} letters')
print('The length of your first name has {} letters:'.format(name.find(' ')))
print(f'The length of your fist name has {name.find(" ")} letters')
c = (name.find(' '))
print(f'The length of your first name has {c} letters')
"""#Or, you can do it in another away:
name = str(input('Enter your full name, please: '))
print(name.upper())
print(name.lower())
name2 = name
name = name.split()
name = ''.join(name)
print(len(name))
name2 = name2.split()
print(len(name2[1]))
#"""













