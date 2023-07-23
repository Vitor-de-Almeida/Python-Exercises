"""create a program that reads any sentence and says if it is a palindrome, disregarding the spaces."""
s = str(input('\033[1;34mEnter a random phrase:\033[m ')).strip()
word = s
word2 = s.replace(' ', '')
s = s.lower().replace(' ', '')
inv = s[::-1]
g = len(s)
e = g
d = 0
count = 0
for c in range(0, g):
    if s[(g-e)] == s[((g-1)-d)]:
        e = e - 1
        d = d + 1
        count += count + 1
print(f'\033[1;33mThe inverse of {word2} is {inv}!\033[m')
if d >= g:
    print(f'\033[1;32mThe word {word} is a palindrome!\033[m')
else:
    print(f'\033[1;32mThe word {word} is not a palindrome!\033[m')
