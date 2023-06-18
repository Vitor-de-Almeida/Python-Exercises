#make an algorithm that reads a temperature in celsius and output its temperature in farenheit
t = float(input('Enter temperature in celsius: '))
f = 9*t/5+32
print(f'The {t:.1f} celsius degrees corresponding to {f:.1f} farenheit degrees')