#create a program that reads a person's name and says if they have "Smith" in their name.
n = str(input("Enter a full name: ").strip())
print(f'Seu nome tem Smith? {"SMITH" in n.upper()}')
