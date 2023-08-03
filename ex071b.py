"""Create a program that simulates the operation of an ATM.
At first, ask the user what will be the amount to be withdrawn (integer number) and the program will inform how many
bills of each value will be delivered. NOTE: Assume that the cashier has $50, $20, $10, and $1 bills."""

print('\033[1;33m=\033[m'*25)
print('\033[1;34mWelcome to the Bank of VR\033[m')
print('\033[1;33m=\033[m'*47)
n = int(input('\033[1;34mWhat amount do you want to withdraw in dollars? \033[m'))
amount = n
bill = 50
totalbill = 0
while True:
    if amount >= bill:
        amount -= bill
        totalbill += 1
    else:
        if totalbill > 0:
            print(f'\033[1;36mTotal of {totalbill} bills of ${bill} dollars\033[m')
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        totalbill = 0
        if amount == 0:
            break
print('\033[1;33m=\033[m'*14)
print('\033[1;33mWelcome back!\033[m')
print('\033[1;33m=\033[m'*14)




