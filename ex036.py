"""Write a program to approve the bank loan for the purchase of a house. The program will ask for the value of the
house, the buyer's salary and in how many years he will pay. Calculate the amount of the monthly installment,
knowing that it cannot exceed 30% of the salary or else the loan will be denied."""
print('\033[1;34mWelcome to Canada Royal Bank! Do you want to see our plans to buy a house? We hope so! \033[m')
print('\033[1;34mNow, we will ask you some questions to analyze your financial profile\033[m')
h = float(input('\033[1;34mWhat is the price in dollars you intend to pay in your house?\033[m '))
s = float(input('\033[1;34mWhat is your current monthly wage in dollars?\033[m '))
y = float(input('\033[1;34mHow many years you want to pay the house?\033[m '))
ym = y*12
installment = float((h / ym))
if installment <= ((s*30)/100):
    print(f'\033[1;34mCongratulations. You can buy a house with us. The loan of your house will'
          f' be {installment:.1f} dollars per month\033[m ')
else:
    print('\033[1;34mCanada Royal Bank appreciate your intention to finance your home with us!'
          'You current wage can not afford the monthly price of this house. We are available!')


