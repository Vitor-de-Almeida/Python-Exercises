"""#Among for students, a professor wants to raffle the order of presentation of schoolwork.
Make a program that helps him, reading their name and showing the order sorted."""
from random import shuffle
n1 = str(input('Enter the name of the first student:'))
n2 = str(input('Enter the name of the second student:'))
n3 = str(input('Enter the name of the third student:'))
n4 = str(input('Enter the name of the fourth student:'))
student = [n1, n2, n3, n4]
shuffle(student)
print(f'The order of the sorted list is:{student}')