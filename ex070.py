"""Make a program that reads the name and the cost of many products.
The program must ask the user if he will continue. At the end, show on the screen:
a - the total cost of the buying.
b - how many products costs above $ 1000.
c - Which is the name of lowest price product.
"""
totalprice = 0
thousand = 0
cheap = 999999999999
namecheap = ''
cont = ''
while True:
    print('\033[1;37m=*=\033[m'*17)
    name = str(input('\033[1;34mEnter the name of the product: \033[m')).strip()
    price = float(input('\033[1;31mEnter the price of the product you want: \033[m'))
    cont = str(input('\033[1;32mDo you want to continue? [Y/N]\033[m')).strip().lower()[0:2]
    while cont not in 'y' and cont not in 'n':
        cont = str(input('\033[1;32mDo you want to continue? [Y/N]\033[m')).strip().lower()[0:2]
        print(cont)
    totalprice += price
    if price > 1000:
        thousand += 1
    if price < cheap:
        cheap = price
        namecheap = name
    if cont == 'n':
        break
print('\033[1;37m=*=\033[m'*17)
print(f'\033[1;33mThe total costs of the buying is {totalprice} dollars!\033[m')
if thousand == 1:
    print(f'\033[1;33mThere is {thousand} product above $ 1000 dollars!\033[m')
else:
    print(f'\033[1;33mThere are {thousand} product above $ 1000 dollars!\033[m')
print(f'\033[1;33mThe name of the cheapest product is {namecheap} which costs {cheap}!\033[m')
print('\033[1;37m=*=\033[m'*17)

