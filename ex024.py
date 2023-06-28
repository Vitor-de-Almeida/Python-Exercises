#create a program that reads the name of a city and says whether or not it starts with the name "Saint"
c = str(input('Enter the name of a city:').strip())
print(c[:5] == 'Saint')
