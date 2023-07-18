"""create a program that reads any sentence and says if it is a palindrome, disregarding the spaces."""
s = str(input('\033[1;34mEnter a random phrase:\033[m '))
g = len(s)
e = g
d = 0
print(g)
print(e)
print(d)
for c in range(0, g):
    if s[g-e] == s[g-d]:
        '''e = e - 1
        d = d + 1'''
        print(f'The word {s} is a palindrome!')
    else:
        print(f'The word {s} is not a palindrome!')
