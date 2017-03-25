dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'}, {'name': 'Garfield',
                        'food': 'lasanga'}, {'name': 'Walter',
                                             'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"


def string_factory(list1, list2):
    sentences = []
    for item in list1:
        sentences.append(list2.format(**item))
    return sentences


string_factory(dicts, string)
