from textwrap import dedent

from player import Player
from room import Room
from item import Item

# Declare all the rooms

room = {
  'outside': Room(
    'Outside Cave Entrance',
    'North of you, the cave mount beckons',
    [Item('Flashlight', 'An electric torch.')]),
  'foyer': Room(
    'Foyer',
    '''Dim light filters in from the south.
    Dusty passages run north and east.''',
    [
      Item('Mask', 'A covering for all or part of the face, worn as a disguise, or to amuse or frighten others.'),
      Item('Helmet', 'A hard or padded protective hat, various types of which are worn by soldiers, police officers, motorcyclists, sports players, and others.'),
    ]),
  'overlook': Room(
    'Grand Overlook',
    '''A steep cliff appears before you, falling into the darkness.
    Ahead to the north, a light flickers in the distance, but there is no way across the chasm.''',
    [
      Item('Rope', 'A length of thick strong cord made by twisting together strands of hemp, sisal, nylon, or similar material.'),
      Item('Hammer', 'A tool with a heavy metal head mounted at right angles at the end of a handle, used for jobs such as breaking things and driving in nails.'),
      Item('Gloves', 'A covering for the hand worn for protection against cold or dirt and typically having separate parts for each finger and the thumb.')
    ]),
  'narrow': Room(
    'Narrow Passage',
    '''The narrow passage bends here from west to north.
    The smell of gold permeates the air.''',
    [
      Item('Knife', 'An  instrument composed of a blade fixed into a handle, used for cutting or as a weapon.'),
      Item('Compass', 'An instrument containing a magnetized pointer which shows the direction of magnetic north and bearings from it.'),
      Item('Watch', 'A small timepiece worn typically on a strap on one\'s wrist.'),
      Item('Map', 'A diagrammatic representation of an area of land or sea showing physical features, cities, roads, etc.')
    ]),
  'treasure': Room(
    'Treasure Chamber',
    '''You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.''',
    [
      Item('Boots', 'A sturdy item of footwear covering the foot and ankle, and sometimes also the lower leg.'),
      Item('Vest', 'An undergarment worn on the upper part of the body, typically having no sleeves.'),
      Item('Bottle', 'A glass or plastic container with a narrow neck, used for storing drinks or other liquids.'),
      Item('Glasses', 'A pair of lenses set in a frame resting on the nose and ears, used to correct or assist defective eyesight.'),
      Item('Wallet', 'A pocket-sized flat folding case for holding money and plastic cards.')
    ])
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main

print('''
##############################
# Python II Exploration Game #
##############################
''')

# Make a new player object that is currently in the 'outside' room. 

player = Player(input('Enter your name to begin the game: '), room['outside'])

# Write a loop that:
# Prints the current room name
# Prints the current description (the textwrap module might be useful here).
# Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters 'q', quit the game.

def validate(choice):
  directions = ['n', 's', 'e', 'w']

  if choice not in directions:
    return '\nInvalid input. Please try again.'
  elif not hasattr(player.current_room, choice + '_to'):
    return f'\nYou cannot go that way {player.name}! Please try again.'

while True:
  room_name = player.current_room.name
  room_description = dedent(player.current_room.description)

  print(f'\n{room_name}\n\n{room_description}')

  choice = input('\nEnter n, s, e, or w to continue exploring or q to quit the game: ')

  if choice.lower() == 'q':
    break
  else:
    result = validate(choice)

    if result:
      print(result)
    else:
      player.current_room = getattr(player.current_room, choice + '_to')