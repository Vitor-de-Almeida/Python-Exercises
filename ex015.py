#write a program that asks for the number of km driven by a rented car and the number of days it was rented.
#Calculate the price to pay, knowing that renting a car costs $60 per day and $0.15 per km traveled.
c = str(input('What car did you picked up?:'))
dk = float(input('How many kilometers did you drive?:'))
dr = float(input('How many days did you keep the car?:'))
#total price of the car=pc
pc = dk*0.15 + dr*60
print(f'The car you choose is {c} and you stayed with it for {dr:.1f} days and you drove for {dk:.1f} kilometers.')
print(f'The total price of your current bill is {pc:.1f} dollars!')
