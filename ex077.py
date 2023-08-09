"""sadasd"""
words = ('Learn', 'Programming', 'Language', 'Pythin', 'Course', 'Free', 'Study', 'Practice',
         'Work', 'Market', 'Programmer')
for word in words:
    print(f'\nIn the word {word} we have', end=' ')
    for letter in word:
        if letter in 'aeiou':
            print(letter, end=' ')


