"""#Develop a program that reads the length of three straight and displays on the screen if they can make a triangle"""
l1 = int(input('Enter the first side of the triangle:'))
l2 = int(input('Enter the second side of the triangle:'))
l3 = int(input('Enter the third side of the triangle:'))
if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('The entered sides can make a triangle! Congratulations')
else:
    print('The entered sides can not make a triangle! Try again')
