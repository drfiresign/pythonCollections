words = input('What is the word you want to devowelize?\n')
words = words.split()
finished_words = []

def remove_vowel(vowel):
    for word in words:
        while True:
            try:
                count = 0
                holding_word = word[count]
                holding_word = holding_word.split()
                holding_word.remove(vowel)
            except ValueError:
                finished_words.append(holding_word)
                count += 1
                break

remove_vowel('a')
remove_vowel('e')
remove_vowel('i')
remove_vowel('o')
remove_vowel('u')
remove_vowel('y')

print(finished_words)