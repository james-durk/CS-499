#James Durkin

def intro():
        print('------------------------------')
        print('Cave Diving Adventure Game')
        print('------------------------------')
        print('Collect your 6 pieces of dive gear and defeat the Giant King Crab!')
        print('------------------------------')
        print('Move commands: go North, go South, go East, go West')
        print('------------------------------')
        print("Add to inventory: get 'item name'")
        print('------------------------------')

def movement(current_room, move, rooms):
        #Moving between areas
        current_room = rooms[current_room][move]
        return current_room

def get_item(current_room, move, rooms, inventory):
        inventory.append(rooms[current_room]['item'])
        del rooms[current_room]['item']

def Start():
        rooms = {
                'Dive Shop Lobby': {'North': 'Mask Cleaning Room', 'South': 'Suit Fitting Room',
                                    'East': 'Cave Entrance', 'West': 'Utilities Room'},
                'Mask Cleaning Room': {'South': 'Dive Shop Lobby', 'East': 'Electronics Room', 'item': 'Goggles'},
                'Electronics Room': {'West': 'Mask Cleaning Room', 'item': 'Flashlight'},
                'Utilities Room': {'East': 'Dive Shop Lobby', 'item': 'Rope'},
                'Suit Fitting Room': {'North': 'Dive Shop Lobby', 'East': 'Tank Storage Room', 'item': 'Wetsuit'},
                'Tank Storage Room': {'West': 'Suit Fitting Room', 'item': 'Oxygen-Tank'},
                'Cave Entrance': {'West': 'Dive Shop Lobby', 'North': 'Cave Depths', 'item': 'Laser-Cutter'},
                'Cave Depths': {'South': 'Cave Entrance', 'item': 'Giant King Crab'}
        }

        #inventory Tracker
        inventory = []
        #Set Starting Room
        current_room = 'Dive Shop Lobby'


        #Display Starting Instructions
        intro()

        while True:
                if current_room == 'Cave Depths':
                        if len(inventory) == 6:
                                print('Congratulations! You defeated the Giant King Crab!')
                                print('Thanks for playing!')
                                break

                        else:
                                print("You didn't collect all of your gear died! Oops!")
                                print('Thanks for playing!')
                                break


                #Current Room and Inventory
                print('You are in the ' + current_room)
                print(inventory)

                #Check current room and items in the room

                if current_room != 'Cave Depths' and 'item' in rooms[current_room].keys():
                        print('You see the {}'.format(rooms[current_room]['item']))

                print('------------------------------')

                move = input('Enter your move: ').title().split()

                #move to next room
                if len(move) >= 2 and move[1] in rooms[current_room].keys():
                        current_room = movement(current_room, move[1], rooms)
                        continue

                #get item to add to inventory
                elif len(move[0]) == 3 and move[0] == 'Get' and ''.join(move[1:]) in rooms[current_room]['item']:
                        print('You pick up the {}'.format(rooms[current_room]['item']))
                        print('------------------------------')
                        get_item(current_room, move, rooms, inventory)
                        continue
                else:
                        print('Invalid move, please try again')
                        continue

Start()



