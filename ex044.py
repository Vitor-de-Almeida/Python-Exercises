"""Make a program that calculate the price to be paid for one product considering it's normal price e payment
condition
- In cash or check: 10% off (discount)
- In cash on card: 5% off
- 2x (two months to pay) in cash on card: normal price (no discount)
- 3x or more in cash on card: 20% of fees"""
price = float(input('\033[1;32mEnter the price of your product in dollars:\033[m '))
method = str(input('\033[1;34mEnter the form of payment you want to use. Please write a, b, c or d option:\n'
                   '-a) In cash or check: 10% off (discount)\n'
                   '-b) In cash on card: 5% off\n'
                   '-c) 2x (two months to pay) in cash on card: normal price (no discount)\n'
                   '-d) 3x or more in cash on card: 20% of fees\n ')).upper()
c1 = int((price*90)/100)
c2 = int((price*95)/100)
c3 = int((price*50)/100)
c4 = int((price*120)/100)/3
if method == 'A':
    print(f'\033[1;34mYou have to pay R$ {c1} dollars in your product. You got 10% off!\033[m')
elif method == 'B':
    print(f'\033[1;35mYou have to pay R$ {c2} dollars in your product. You got 5% off!\033[m')
elif method == 'C':
    print(f'\033[1;36mYou have to pay in two months R$ {c3} dollars in your product. You got no discount!'
          f' Total of product R$ {int(c3*2)} dollars \033[m')
elif method == 'D':
    print(f'\033[1;31mYou have to pay in three months R$ {c4} dollars in your product. You got fees of 20%!'
          f' Total of product R$ {int(c4*3)} dollars \033[m')


