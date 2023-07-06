"""#Make a program that reads the speed of a car.
If he exceeds 80 km/h, show him on the screen a message that he got a fine.
The fine will cost 30 dollars by km exceeded"""
v = float(input('Enter the velocity of the car right now:'))
if v > 80:
    n = ((v-80)*30)
    print(f'You received a fine in the amount of {n} dollars!')
else:
    print('Congratulations, you are a conscientious driver! You are on the road speed limit.')
