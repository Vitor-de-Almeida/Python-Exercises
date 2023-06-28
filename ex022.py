#create a program that reads a person's full name and displays it on the screen
name = str(input('Enter your full name, please: '))
print(name.upper())
print(name.lower())
print(len(name.replace(' ', '')))
print(len(name.split()[0]))
"""#Or, you can do it in another away:'''"""
name = str(input('Enter your full name, please: '))
print(name.upper())
print(name.lower())
name2 = name
name = name.split()
name = ''.join(name)
print(len(name))
name2 = name2.split()
print(len(name2[1]))
#













