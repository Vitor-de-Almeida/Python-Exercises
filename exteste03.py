words = ('Learn', 'Programming', 'Language', 'Python', 'Course', 'Free', 'Study', 'Practice',
         'Work', 'Market', 'Programmer')

vowels = ('a', 'e', 'i', 'o', 'u')

for word in words:
    vowel_positions = [word.find(vowel) for vowel in vowels]
    vowel_positions = [pos for pos in vowel_positions if pos != -1]

    vowel_letters = [word[pos] for pos in vowel_positions]
    vowels_str = ' '.join(vowel_letters)

    print(f'In the word {word} we have {vowels_str}')