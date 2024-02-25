# the text for the introduction
def introduction(name, gfName):
    print('Hangry GF\n'
          'By: Nicholas A. DaRosa\n\n\n')

    print('it is the 22nd of january, you wake at 10 am in a cold sweat and panic,\n')
    print(f'I didnt make ' + gfName + ' breakfast!!')
    print(
        'Before the thought can finish in your head, you hear a loud bellowing grumble of a stomach... \n\nand then you see her,\n\n'
        'sitting in a chair in the corner of the room, beet red and furious\n\n'
        '"', name + '!!! TO MORENDO DE FOME!!!” she screams in Brazilian Portuguese “IM DYING OF HUNGER!!" \n\n')
        'She reaches into the dresser cabinet and pulls out a chancla.\n'
        'Your quick thinking skills kick from years of playing FordKnight in and you dodge roll out of the room\n'
        ' and lock the door before the airborne sandal gets lodged into the door, inches away from your face.\n\n'
        'your infuriated girlfriend is now a ravenous Brazilian demon with a bottomless appetite.\n'
        " The only way that you can sate the beast's appetite and get your sweetheart back \n"
        " is by collecting all of the ingredients to make\n"
        ' a sacred "Misto Quente" ( ham and cheese )  sandwich with a fried egg  and ALOT of garlic powder\n\n'
        "You will find the eggs in the fridge in the basement,\n the garlic powder is in the pantry,\n"
        " the bread is in the dining room,\n"
        " and the ham and cheese in the kitchen fridge.\n"
        " You must collect all of these ingredients,\n"
        " along with Cookware in the kitchen and cook them on the grill outside.\n"
        " Only when the glorious brunch is complete can you re-enter the room\n"
        " to rescue your princess from the demon that lies within her.")


# Moves the player to an adjacent room in the given direction.
# input is the current room you are in and the direction you would like to travel in
# Returns The new room the player is in.

def move_room(current_room, direction):
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        print(f"You are now in the {current_room}")

    else:
        print(f'You try to move {direction}')
        print("You cannot move in that direction.")
    return current_room


def get_item():
    print('FIXME: build instructions to grab item if the user types "Get Item"')


# The map of HangryGF to refer to when moving and collecting items
rooms = {
    'Hall': {'north': 'Dining Room', 'east': 'Pantry', 'west': 'Basement', 'msg': 'you are in the Hall.\n'
                                                                                  'To the North is the Dining Room,\n'
                                                                                  'To the south is the bedroom(locked),\n'
                                                                                  'To the East is the Pantry,\n'
                                                                                  'And to the West'},
    'Bedroom': {'north': 'Hall', 'boss': 'Hangry GF'},
    'Basement': {'east': 'Hall', 'item': 'Eggs'},
    'Pantry': {'west': 'Hall', 'item': 'Garlic'},
    'Dining Room': {'north': 'Bathroom', 'south': 'Hall', 'east': 'Backyard', 'west': 'Kitchen', 'item': 'Bread'},
    'Backyard': {'west': 'Dining Room', 'item': 'Grill'},
    'Bathroom': {'south': 'Dining Room', 'item': 'Cookware'},
    'Kitchen': {'east': 'Dining Room', 'west': 'Fridge', 'item': 'Ham'},
    'Fridge': {'east': 'Kitchen', 'item': 'Cheese'}
}
