# and returns a tuple of four versions of the string:
# uppercased, lowercased, titlecased
# (where every word's first letter is capitalized),
# and a reversed version of the string.

# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice?


def stringcases(str):
    a = str.upper()
    b = str.lower()
    c = str.title()
    d = str[-1::-1]
    return (a, b, c, d)


print(stringcases("sopHie the cat"))
