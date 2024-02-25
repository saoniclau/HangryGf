#Nicholas DaRosa
#IT-140
#Southern New Hampshire University
#02/24/2024
####################################################################################
#
import sys,time,random

####################################################################################
#Defining Functions


# the text for the introduction
def introduction(name, gfName):
    print('Hangry GF\n'
          'By: Nicholas A. DaRosa\n Art by: Lgbeard\n\n\n')

    print('it is the 22nd of january, you wake at 10 am in a cold sweat and panic,\n')
    print(f'I didnt make ' + gfName + ' breakfast!!')
    print_slow('******\n')
    print(
        'Before the thought can finish in your head, you hear a loud bellowing grumble of a stomach... \n\nand then you see her,\n\n'
        'sitting in a chair in the corner of the room, beet red and furious\n\n'
        '"', name + '!!! TO MORENDO DE FOME!!!” she screams in Brazilian Portuguese “IM DYING OF HUNGER!!" \n\n'
        'She reaches into the dresser cabinet and pulls out a chancla.\n'
        'Your quick thinking skills kick from years of playing FordKnight in and you dodge roll out of the room\n'
        ' and lock the door before the airborne sandal gets lodged into the door, inches away from your face.\n\n')
    print_slow('************ \n\n')
    print('your infuriated girlfriend is now a ravenous demon with a bottomless appetite.\n'
        " The only way that you can sate the beast's appetite and get your sweetheart back \n"
        " is by collecting all of the ingredients to make\n"
        ' a sacred "Misto Quente" ( ham and cheese )  sandwich with a fried egg  and ALOT of garlic powder\n\n')
    print_slow('*************                    \n\n')
    print("You will find the eggs in the basement.\nThe garlic powder is in the pantry,\n"
        "the bread is in the dining room,\nThe Ham is in the kitchen.\n"
        "The Cheese is in the fridge.\nThe Cookware seems to be hidden somewhere...")
    print_slow('                           \n')
    print(" You must collect all of these ingredients, then go the the grill in the Backyard to make the sandwich\n")
    print_slow("until you have made the sandwich          \nDon't Go In The Bedroom!!\n\n")


def rules():
    global recipe
    global inventory
    missing = list(set(recipe) - set(inventory))

    print("""Collect all 6 ingredients and cook them on the grill to feed your hangry girlfriend…\nBefore she EATS YOU!\n\n
          To travel in a direction, write "go", "move", "travel", "walk", "traverse" followed by a direction. \n
          To pick up an item, write either 'get', 'grab', 'take', or 'store' and the name of the item\n
          I.E. "Go North", or "Get Bread"\n\n""")
    print(f'you are missing: {missing}')




#the "normalize__" functions checks a string (cmd) for words in the the list with the same meaning and returns one word.
#if the string is not a list item when lowercase, return the original string
def normalize_go_command(cmd):
    if cmd.lower() in ['go', 'move', 'travel', 'walk', 'traverse']:
        return 'go'
    else:
        return cmd

def normalize_get_command(cmd):
    if cmd.lower() in ['get', 'grab', 'take', 'store']:
        return 'get'
    else:
        return cmd
def normalize_cook_command(cmd):
    if cmd.lower() in ['grill', 'cook', 'make']:
        return 'grill'
    else:
        return cmd


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


##FIXME:
def get_item(current_room):
    global inventory
    if inventory is None:
        inventory = []
    if rooms[current_room].get('item') not in inventory:
        inventory.append(rooms[current_room]['item'])
    else:
        print(f'you try to grab {rooms[current_room]["item"]}')
        print("you already have one. don't be wasteful")

def cook_sandwich(room):
    global inventory
    global recipe
    print('test', inventory)
    recipe = ['Garlic', 'Eggs', 'Bread', 'Cookware', 'Ham', 'Cheese']
    if room == 'Backyard':
        result = all(elem in inventory for elem in recipe)
        print(result)
        if result == True:
            print('Sandwich Aquiesed!!')
            inventory.append('Misto Quente')
        else:
            print('You are missing something')
    else:
        print('This isnt the place to play with fire. Do that in the backyard')

#slow typing function I got from stack overflow
typing_speed = 60 #wpm
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def boss_fight(items):
    global action
    #check inventory for Misto queso
    if 'Misto Quente' in items:
        # game ending if you win (misto queso in inventory)
        print("the glowing red eyes approach you from the dark corner of the room to reveal a hideous monster")
        print_slow("                ")
        print("""  
                            ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \ 
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._  0`\ \ |  //'0  _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \ \`\ |  |  | /,//' \,'  \ 
            /   /     ||--+--|--+-/-|     \   \ 
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
                                                """)
        print_slow(f"{name}.... I...... aM ........ FaAmmIssSHed...               \n")
        print('Before you can respond, she CHARGES at you.')
        print_slow("           \nFAAAAAAMMMIIIIIIIIIISSSHHHED               \n")
        print("you throw the sandwich into the demons gaping mouth just as it tackles you to the ground.\n")
        print_slow('        ')
        print('silence')
        print_slow('                     \n')
        print('PPFFFFFTT')
        print_slow("          \n.....thank....you.......\n")
        print('''       .--.
      /`._ `.
     | /. .` \ 
     / ) _ ( /
    | /.`-' \-.
    / )`.   (  \ 
    | .  \^  \ |
    | |`. \`-| |
    //   ' \`\ |
   .'    .\ .| |
  /   ``-._`.`-.
  |        `-._ `.
   `.._.----`  `.'
 _.--`      _.-'
'.__..--````    ''')
        print('You Did It! You saved the day and got your beautiful gf back!!')
        print_slow(" One thing.........\n You forgot to make yourself breakfast too.....")
        action = ["exit", 'game']




    else:
        #if you lose(misto queso not in inventory)
        print("the glowing red eyes approach you from the dark corner of the room to reveal a hideous monster")
        print("""  
                                    ,-.
               ___,---.__          /'|`\          __,---,___
            ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
          ,'        |           ~'\     /`~           |        `.
         /      ___//              `. ,'          ,  , \___      \ 
        |    ,-'   `-.__   _         |        ,    __,-'   `-.    |
        |   /          /\_  `   .    |    ,      _/\          \   |
        \  |           \ \`-.___ \   |   / ___,-'/ /           |  /
         \  \           | `._  0`\ \ |  //'0  _,' |           /  /
          `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
             ``       /     \    ,='/ \`=.    /     \       ''
                     |__   /|\_,--.,-.--,--._/|\   __|
                     /  `./  \ \`\ |  |  | /,//' \,'  \ 
                    /   /     ||--+--|--+-/-|     \   \ 
                   |   |     /'\_\_\ | /_/_/`\     |   |
                    \   \__, \_     `~'     _/ .__/   /
                     `-._,-'   `-._______,-'   `-._,-'
                                                        """)
        print_slow(f"{name}.... I...... aM ........ FaAmmIssSHed...               \n")
        print('Before you can respond, she CHARGES at you.')
        print_slow("           \n FAAAAAAMMMIIIIIIIIIISSSHHHED              \n ")
        print('Before you can get away, you are eaten in one gulp\n')
        print_slow("    \nYOU ARE DEAD!       ")
        action = ["exit", 'game']



################################################################################
#
# The map of HangryGF to refer to when moving and collecting items
rooms = {
    'Hall': {'north': 'Dining Room', 'east': 'Pantry','south': 'Bedroom', 'west': 'Basement', 'item':'dust', 'msg': 'you are in the Hall.\n'
                                                                                                                    'nothing special...\n\n'
                                                                                  'To the north is the Dining Room,\n'
                                                                                  'To the south is the Bedroom,\n'
                                                                                  'To the east is the Pantry,\n'
                                                                                  'And to the west is the Basement'},
    'Bedroom': {'north': 'Hall', 'boss': 'Hangry GF', 'msg': 'You are in the Bedroom.\n'
                                                      'your Hangry GF lies in wait, eagerly anticipating your next move.\n'},
    'Basement': {'east': 'Hall', 'item': 'Eggs', 'msg':
                                                      'It smells like mildew and mold,\n'
                                                      'there is a carton of Eggs in a cooler,\n'
                                                      'To the east is the Hall,\n'
                                                      },
    'Pantry': {'west': 'Hall', 'item': 'Garlic', 'msg':
                                                      'It smells like spices and cleaning agents.\n'
                                                      'There is a clove of Garlic on a shelf\n'
                                                      'To the west is the Hall.\n'
                                                      },
    'Dining Room': {'north': 'Bathroom', 'south': 'Hall', 'east': 'Backyard', 'west': 'Kitchen', 'item': 'Bread', 'msg':
                                                      'The morning sun is shining through the Backyard sliding doors,\n'
                                                      'there is a freshly baked loaf of bread on the Dining room table.\n\n'
                                                      'To the south is the Hall,\n'
                                                      'to the east is the Backyard,\n'
                                                      'and to the west is the Kitchen'},
    'Backyard': {'west': 'Dining Room', 'item': 'Dog Poop', 'cook': 'Misto Quente', 'msg':
                                                      'The grass is a bit overgrown, and theres dog poop everywhere...\n'
                                                      'you dont have a dog.\n\n' 
                                                      'There is a Grill on the porch. To use it, type "grill sandwich"\n'
                                                      'to the west is the Dining Room'},
    'Bathroom': {'south': 'Dining Room', 'item': 'Cookware', 'msg':
                                                      'The cleanest room in the house\n'
                                                      'Odd.. someone left all of the cookware on the sink.\n'
                                                      'To the south is the Dining Room.\n'
                                                      },
    'Kitchen': {'east': 'Dining Room', 'west': 'Fridge', 'item': 'Ham', 'msg':
                                                      'your favorite place to be (besides with your GF *who you love very much*)\n'
                                                      'there is a massive slab of deli ham on the counter\n\n'
                                                      'To the east is the Dining Room,\n'
                                                      'And to the west is the Fridge'},
    'Fridge': {'east': 'Kitchen', 'item': 'Cheese', 'msg':
                                                      'the ice maker is broken...along with the lightbulb \n'
                                                      'There is an industrial-sized block of government cheese on the middle rack.\n\n'
                                                      'To the east is the Kitchen.'
                                                      }
}

###################################################################################
#Variables and lists

#yours and your gf's name
name = str(input('What is your name?: '))
gfName = str(input('What is your significant others name?: '))

#your current room. you will start the game in the hall.
current_room = 'Hall'

#initialize the action and the inventory lists.
action = ["",""]
inventory = []
#recipe for a misto queso
recipe = ['Cookware', 'Garlic', 'Eggs', 'Bread',  'Ham', 'Cheese']
###################################################################################
#gameplay

introduction(name, gfName)
print()
print()

#gameplay loop iterates until the action list contains exit
while action and action[0].lower() != 'exit':
    #test to see the action list and its length
    #print(action, len(action))

    #print the msg value in the current room
    print(rooms[current_room]['msg'])

    #save players next move in the list "action", then checks the first list item for valid commands
    action = input('What is your next move?? ').split(' ')
    action[0] = normalize_go_command(action[0])
    action[0] = normalize_get_command(action[0])
    action[0] = normalize_cook_command(action[0])
    print()

    #timed typing to simulate the timelapse of the player walking to do the action
    print('Walking')
    print_slow('*****\n')
    #checks if the action list doesnt have 2 variables
    if len(action) !=2:
        print('I dont understand. please enter "go"/"get", followed by a direction/item./n if you need help, enter "show rules"')
    #opens the rules
    elif 'help' in action:
        print(rules())
    # check for 'grill'
    elif 'grill' in action:
        cook_sandwich(current_room)
    elif 'get' in action[0] or rooms[current_room]["item"] in action[1]:
        get_item(current_room)
        print(f'you have:{inventory}')
    #moves you in direction respective to your location on the map
    elif 'go' in action:
        current_room = move_room(current_room, action[1])
        #checks if you have entered the bedroom. if so, initiates the boss fight.
        if current_room == "Bedroom":
            boss_fight(inventory)
        else:
            pass
    #
    else:
        print('incorrect direction, try again')
    print()
    print()


print('''
'  _,  _, _, _ __,    _, _,_ __, __, '
' / _ / \ |\/| |_    / \ | / |_  |_) '
" \ / |~| |  | |     \ / |/  |   | \ "
'  ~  ~ ~ ~  ~ ~~~    ~  ~   ~~~ ~ ~'
                                   ''')