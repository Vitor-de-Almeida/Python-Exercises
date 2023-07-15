"""Develop a logic that reads a person's weight and height, calculates their BMI and displays their status,
according to the table below:
- Under 18.5: Underweight;
- Between 18.5 and 25: Ideal weight;
- 25 to 30: Overweight;
- 30 to 40: Obesity;
- Above 40: Morbid obesity."""
w = float(input('\033[1;34mEnter your current weight in kilogram:\033[m '))
h = float(input('\033[1;34mEnter your current height in meters:\033[m '))
BMI = (w / (h**2))
if BMI < 18.5:
    print(f'\033[1;31mYou are Underweight! You need to eat more! Your BMI are {BMI:.2f}\033[m')
elif 18.5 <= BMI < 25:
    print(f'\033[1;32mYou are in the ideal weight! Your BMI are {BMI:.2f}\033[m')
elif 25 <= BMI < 30:
    print(f'\033[1;33mYou are Overweight! You need to eat less and practice exercises! Your BMI are {BMI:.2f}\033[m')
elif 30 <= BMI < 40:
    print(f'\033[1;35mYou are obese! You need a diet! Your BMI are {BMI:.2f}\033[m')
else:
    print(f'\033[1;36mYou are overweight! You need are morbidly obese! Your BMI are {BMI:.2f}\033[m')

