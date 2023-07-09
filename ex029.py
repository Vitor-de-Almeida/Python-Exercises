"""#Make a program that reads the speed of a car.
If he exceeds 80 km/h, show him on the screen a message that he got a fine.
The fine will cost 30 dollars by km exceeded"""
v = float(input('Enter the velocity of the car right now:'))
if v > 80:
    n = ((v-80)*30)
    print('\033[1;31mBe careful\033[m, you exceed the speed limit of \033[1;30;107m80 km/h\033[m')
    print(f'You received a fine in the amount of \033[1;31m{n:.2f}\033[m dollars!')
else:
    print('Congratulations, you are a conscientious driver! You are on the road \033[1;34m80\033[m km/h speed limit.')
