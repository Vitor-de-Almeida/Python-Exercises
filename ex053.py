"""create a program that reads any sentence and says if it is a palindrome, disregarding the spaces."""
s = str(input('\033[1;34mEnter a random phrase:\033[m ')).strip()
word = s
s = s.lower().replace(' ', '')
g = len(s)
e = g
d = 0
count = 0
for c in range(0, g):
    if s[(g-e)] == s[((g-1)-d)]:
        e = e - 1
        d = d + 1
        count += count + 1
        if d >= g:
            print(f'The word {word} is a palindrome!')
    else:
        print(f'The word {word} is not a palindrome!')