"""#Develop a program that asks the user how far he wants to travel in kilometers (km).
Calculate the ticket price, charging $0.50 per km for trips up to 200 km and $0.45 for trips over 200 km."""
dist = float(input("\033[1;97;40mWhat is the distance in kilometers that you intend to travel?\033[m "))
if dist <= 200:
    v1 = dist*0.50
    print(f'Your ticket trip will cost you {v1:.1f} dollars!')
else:
    v2 = dist*0.45
    print(f'Your ticket trip will cost you {v2:.1f} dollars!')
