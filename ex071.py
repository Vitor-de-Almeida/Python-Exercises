"""Create a program that simulates the operation of an ATM.
At first, ask the user what will be the amount to be withdrawn (integer number) and the program will inform how many
bills of each value will be delivered. NOTE: Assume that the cashier has $50, $20, $10, and $1 bills."""
print('\033[1;33m=\033[m'*25)
print('\033[1;34mWelcome to the Bank of VR\033[m')
print('\033[1;33m=\033[m'*47)
n = int(input('\033[1;34mWhat amount do you want to withdraw in dollars? \033[m'))
c50a = n // 50
c50b = n % 50
c20a = c50b // 20
c20b = c50b % 20
c10a = c20b // 10
c10b = c20b % 10
c1a = c10b // 1
c1b = c10b % 1
print(f'\033[1;36mTotal of {c50a} bills of $50\033[m')
print(f'\033[1;36mTotal of {c20a} bills of $20\033[m')
print(f'\033[1;36mTotal of {c10a} bills of $10\033[m')
print(f'\033[1;36mTotal of {c1a} bills of $1\033[m')
print('\033[1;33m=\033[m'*34)
print('\033[1;34mAlways come back to the Bank of VR\033[m')
