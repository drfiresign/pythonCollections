def disemvowel(word):
    deword = []
    for letter in word:
        if letter.lower() not in list('aeiou'):
            deword.append(letter)
        else:
            continue
    return ''.join(deword)

print(disemvowel('i am QUEUEING in a queue'))
