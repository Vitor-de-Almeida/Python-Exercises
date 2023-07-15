"""#Develop a program that reads the length of three straight and displays on the screen if they can make a triangle
and what is the type of it"""
l1 = float(input('\033[1;34mEnter the first side of the triangle: \033[m'))
l2 = float(input('\033[1;34mEnter the second side of the triangle: \033[m'))
l3 = float(input('\033[1;34mEnter the third side of the triangle: \033[m'))
if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('\033[1;36mThe entered sides can make a triangle! Congratulations\033[m')
    if l1 == l2 == l3:
        print(f'\033[1;33mAll the three sides make an equilateral triangle!\033[m')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print(f'\033[1;32mAll the three sides make an isosceles triangle!\033[m')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print(f'\033[1;31mAll the three sides are different and make an scalene triangle!\033[m')
else:
    print('\033[1;34mThe entered sides can not make a triangle! Try again\033[m')