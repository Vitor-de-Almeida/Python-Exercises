"""Create a program that has a fully populated tuple with a count spelled out from zero to twenty.
Your program should read a number from the keyboard (between 0 and 20) and display it in full."""
import number2word
number = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
          'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
          'Nineteen', 'Twenty')
n = int(input('\033[1;34mEnter an integer between 0 and 20: \033[m'))
while True:
    if not 0 <= n <= 20:
        n = int(input('\033[1;34mTry again. Enter an integer between 0 and 20: \033[m'))
    else:
        print(f'\033[1;32mYou entered the number {number[n]} !\033[m')
        break


