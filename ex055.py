"""create a program that reads the weight of five people. At the end, show the bigger and the lower weight"""
bigger = 0
lower = 0
for p in range(1, 6):
    w = float(input(f"\033[4;97;43mEnter the {p}ª person's weight:\033[m "))
    if p == 1:
        bigger = w
        lower = w
    else:
        if w > bigger:
            bigger = w
        elif w < lower:
            lower = w
print(f'\033[4;36;40mThe bigger weight is {bigger} and the lower weight is {lower}\033[m')
