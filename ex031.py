"""#Develop a program that asks the user how far he wants to travel in kilometers (km).
Calculate the ticket price, charging $3 per km for trips up to 200 km and $2 for trips over 200 km."""
dist = float(input("What is the distance in kilometers that you intend to travel?"))
if dist <= 200:
    v1 = dist*3
    print(f'Your ticket trip will cost you {v1} dollars!')
else:
    v2 = dist*2
    print(f'Your ticket trip will cost you {v2} dollars!')
