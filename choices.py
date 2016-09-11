from random import choice


def nchoices(iterable, n):
    output = []
    while n > 0:
        output.append(choice(iterable))
        n -= 1
    return output


things = list(range(50))
print(nchoices(things, 50))
