from random import choice


def nchoices(iterable, n):
    output = []
    while n > 0:
        choice(iterable).append(output)
        n -= 1
