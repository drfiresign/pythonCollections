# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.

def word_count(str):
    words = str.lower().split()
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict.update({ word: 1})
    return(words_dict)
