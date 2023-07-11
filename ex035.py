"""#Develop a program that reads the length of three straight and displays on the screen if they can make a triangle"""
l1 = float(input('\033[1;33mEnter the first side of the triangle: \033[m'))
l2 = float(input('\033[1;33mEnter the second side of the triangle: \033[m'))
l3 = float(input('\033[1;33mEnter the third side of the triangle: \033[m'))
if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('\033[1;34mThe entered sides can make a triangle! Congratulations\033[m')
else:
    print('\033[1;34mThe entered sides can not make a triangle! Try again\033[m')
