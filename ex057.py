"""Make a program that reads the gender of one person, but only accept
the value of 'M' or 'F'. If the user enter a wrong value, ask for new value until having the correct one"""
g = str(input('\033[1;34mEnter your gender by using M - Masculine or F - Feminine:\033[m ')).strip().lower()[0]
while g not in 'MmFf':
    g = str(input('\033[1;34mInvalid values. Please, enter your gender by using M - Masculine or F - Feminine:\033[m ')).lower().strip()
print(f'\033[1;32mGender registered successful\033[m')
