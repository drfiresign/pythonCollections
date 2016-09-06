# Create a function named combo() that takes two iterables and returns
# a list of tuples. Each tuple should hold the first item in each list,
# then the second set, then the third, and so on. Assume the iterables
# will be the same length.

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.


def combo(a, b):
    e = []
    for i, j in zip(a, b):
        e.append((i, j))
    return e


combo([1, 2, 3], 'abc')
