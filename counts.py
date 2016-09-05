my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']
# members(my_dict, my_list) => 2


def members(dicty, listy):
    membership = []
    for item in listy:
        try:
            membership.append(dicty[item])
            print("Sucess: " + item)
        except KeyError:
            print("Failure: " + item)
            continue
    return len(membership)

members(my_dict, my_list)
