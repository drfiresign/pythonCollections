import random
import time
import os

CELLS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0),
         (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 0), (2, 1),
         (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 0), (3, 1), (3, 2),
         (3, 3), (3, 4), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3),
         (4, 4), (4, 5), (4, 6), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4),
         (5, 5), (5, 6), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5),
         (6, 6)]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_locations():
    # monster = random
    monster = random.choice(CELLS)
    # door = random
    door = random.choice(CELLS)
    # start = random
    start = random.choice(CELLS)
    player = {'current_loc': start, 'loc': [start]}
    # if monster, door, or start are the same, do it again
    if monster == door or monster == start or door == start:
        return get_locations()
    # return monster, door, start
    return monster, door, player


def move_player(player, move):
    # get player position
    x, y = player['current_loc']
    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1
    return x, y


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player['current_loc']
    if y <= 0:
        moves.remove('LEFT')
    if y >= 6:
        moves.remove('RIGHT')
    if x <= 0:
        moves.remove('UP')
    if x >= 6:
        moves.remove('DOWN')
    return moves


def draw_map(player):
    print(' _ _ _ _ _ _ _')
    tile = '|{}'

    for idx, cell in enumerate(CELLS):
        if idx in [6, 13, 20, 27, 34, 41, 48]:
            if cell == player['current_loc']:
                print(tile.format('X|'))
            elif cell in player['loc']:
                print(tile.format('•|'))
            else:
                print(tile.format('_|'))
        else:
            if cell == player['current_loc']:
                print(tile.format('X'), end='')
            elif cell in player['loc']:
                print(tile.format('•'), end='')
            else:
                print(tile.format('_'), end='')


def run_game():
    while True:
        moves = get_moves(player)

        print("You're currently in room {}".format(player['current_loc']))

        draw_map(player)

        print("\nYou can move {}".format(moves))
        print("Enter QUIT to quit.")

        move = input("> ")
        move = move.upper()

        if move == "QUIT":
            break

        if move in moves:
            player['current_loc'] = move_player(player, move)
            player['loc'].append(player['current_loc'])
        else:
            clear()
            print("""

            *************************************************
            **                                             **
            **   Walls are hard, stop walking into them!   **
            **                                             **
            *************************************************

            """)
            time.sleep(3)
            clear()
            continue
        # if new player position is the door, they win!
        if player['current_loc'] == door:
            clear()
            print("""
You escaped!
A rousing sucess if there ever was one.
Time to head home with your loot.
Ride safe my leige...
            """)
            time.sleep(3)
            clear()
            break

        # if new player position is the monster, they lose!
        if player['current_loc'] == monster:
            clear()
            print("""
As you carefully opened the door,
being sure to check for any possible
sound of the monster, a deep growl escapes,
leaving your party breathless...""")
            time.sleep(2)
            print("""
Before you even feel the pain set in,
the sharp, glinting jaws of your enemy
sink into your neck.""")
            time.sleep(2)
            print("""
Your head pops up and is quickly swallowed by the monster...
            """)
            time.sleep(2)
            print("""
You were eaten by the grue!
A tragic death if there ever was one.
Your body may rot, but your soul will seek peace
\tMay flights of Angels sing thee to they rest...
            """)
            time.sleep(3)
            clear()
            break

        # otherwise, continue
        else:
            clear()
            continue


monster, door, player = get_locations()
clear()
print("Welcome to the Dungeon!")
run_game()

# Ideas to continue:
# * add much larger map
# * create random movement for monster
