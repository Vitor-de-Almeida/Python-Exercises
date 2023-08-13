esc = list()
p1 = 0
p2 = 0
esc.append(str(input('Enter an expression: ')).strip().lower())
for pos in esc[0]:
    if pos == '(':
        p1 += 1
    if pos == ')':
        p2 += 1
if p1 == p2:
    print('The expression is valid')
else:
    print('The expression is invalid')
