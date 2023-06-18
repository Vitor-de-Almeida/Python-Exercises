#create an algorithm that reads a number and outputs its double, triple, and square root.
n1 = float(input ('Say a number: '))
d = (n1*2)
t = (n1*3)
s = (n1**(1/2))
print (f'{n1} double is {d}\n{n1} triple is {t}\n{n1} square root is {s:.2f}!')
print(f'{n1} square root is {pow(n1, (1/2)):.2f}!')


