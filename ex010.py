#create a program that reads how much money a person has in his wallet in reais
#and shows how many dollars he can buy (consider the dollar at $ 4.82)
m = float(input('how much money do you have to buy dollars?: R$'))
c = m/4.82
print(f'With {m:.1f} reais you can buy {c:.1f} dollars!')
