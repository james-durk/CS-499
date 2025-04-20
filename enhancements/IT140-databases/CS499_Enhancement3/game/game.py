from room import Room
from player import Player
from pathfinder import find_shortest_path
from save_manager import SaveManager


class Game:
    def __init__(self):
        """
        Initialize the game with rooms, a player, and the game loop.
        """
        self.rooms = self.create_rooms()
        self.player = Player("Diver", self.rooms["Dive Shop Lobby"])
        self.required_items = {"Goggles", "Flashlight", "Rope", "Wetsuit", "Oxygen Tank", "Laser Cutter"}
        self.save_manager = SaveManager()

    def create_rooms(self):
        """
        Define all rooms and their connections.
        """
        rooms = {
            "Dive Shop Lobby": Room("Dive Shop Lobby", "A cozy dive shop with friendly staff."),
            "Mask Cleaning Room": Room("Mask Cleaning Room", "Shelves are lined with different diving masks.", "Goggles"),
            "Electronics Room": Room("Electronics Room", "Brightly lit and filled with diving gear.", "Flashlight"),
            "Utilities Room": Room("Utilities Room", "Storage of useful diving tools.", "Rope"),
            "Suit Fitting Room": Room("Suit Fitting Room", "Diving suits hang on the racks.", "Wetsuit"),
            "Tank Storage Room": Room("Tank Storage Room", "A warehouse filled with oxygen tanks.", "Oxygen Tank"),
            "Cave Entrance": Room("Cave Entrance", "A dark cave leading into the unknown.", "Laser Cutter"),
            "Cave Depths": Room("Cave Depths", "A mysterious underwater chamber with a Giant King Crab.")
        }

        # Define room connections
        rooms["Dive Shop Lobby"].set_connection("North", rooms["Mask Cleaning Room"])
        rooms["Dive Shop Lobby"].set_connection("South", rooms["Suit Fitting Room"])
        rooms["Dive Shop Lobby"].set_connection("East", rooms["Cave Entrance"])
        rooms["Dive Shop Lobby"].set_connection("West", rooms["Utilities Room"])
        rooms["Mask Cleaning Room"].set_connection("South", rooms["Dive Shop Lobby"])
        rooms["Mask Cleaning Room"].set_connection("East", rooms["Electronics Room"])
        rooms["Electronics Room"].set_connection("West", rooms["Mask Cleaning Room"])
        rooms["Utilities Room"].set_connection("East", rooms["Dive Shop Lobby"])
        rooms["Suit Fitting Room"].set_connection("North", rooms["Dive Shop Lobby"])
        rooms["Suit Fitting Room"].set_connection("East", rooms["Tank Storage Room"])
        rooms["Tank Storage Room"].set_connection("West", rooms["Suit Fitting Room"])
        rooms["Cave Entrance"].set_connection("West", rooms["Dive Shop Lobby"])
        rooms["Cave Entrance"].set_connection("North", rooms["Cave Depths"])
        rooms["Cave Depths"].set_connection("South", rooms["Cave Entrance"])

        return rooms

    def check_win_condition(self):
        """
        Check if the player has won the game by collecting all required items and entering the Cave Depths.
        """
        if self.player.current_room == self.rooms["Cave Depths"] and len(self.player.inventory) >= 6:
            print("Congratulations! You defeated the Giant King Crab!")
            print("Thanks for playing!")
            exit()  # Exit the game loop when the player wins

    def start(self):
        """
        Start the game loop.
        """
        print("Welcome to the Cave Diving Adventure Game!")
        print("Collect all 6 pieces of diving gear to defeat the Giant King Crab!")
        print("Type 'go [direction]' to move, 'get' to pick up an item, 'inventory' to view inventory,")
        print("'find [item]' to get the shortest path to a room containing that item,")
        print("or 'checklist' to see which items remain.")
        print("Use command 'save' to save your progress, or 'load' to resume a saved game.")

        while True:
            print(f"\nYou are in {self.player.current_room.name}")
            print(self.player.current_room.description)
            if self.player.current_room.has_item():
                print(f"You see {self.player.current_room.item}")

            command = input("> ").strip().lower()

            if command.startswith("go "):
                direction = command.split(" ")[1].capitalize()
                self.player.move(direction)
                self.check_win_condition()  # Check after movement
            elif command == "get":
                self.player.pick_up_item()
            elif command == "inventory":
                self.player.show_inventory()
            elif command.startswith("find "):  # BFS algorithm
                target_item = command.split(" ", 1)[1].strip()
                path = find_shortest_path(self.player.current_room, target_item)
                if path:
                    print(f"Shortest path to '{target_item}':")
                    for i in range(len(path) - 1):
                        current_room, direction = path[i]
                        next_room = path[i + 1][0]
                        print(f"From {current_room}, go {direction} to reach {next_room}")
                    print(f"You'll reach {path[-1][0]} where the item is located.")
                else:
                    print(f"Item '{target_item}' not found in any room.")
            elif command == "checklist":  # See items that remain to be collected
                missing_items = self.required_items - set(self.player.inventory)
                if missing_items:
                    print("You still need to collect the following items:")
                    for item in missing_items:
                        print(f" - {item}")
                else:
                    print("You've collected all required items! Go to the Cave Depths!")
            elif command == "save":  # Save method
                self.save_manager.save_game(self.player.current_room.name, self.player.inventory, self.rooms)
            elif command == "load":  # Load method
                loaded_room, loaded_inventory, loaded_room_items = self.save_manager.load_game()
                if loaded_room:
                    self.player.current_room = self.rooms[loaded_room]
                    self.player.inventory = loaded_inventory
                    # Update room items
                    for room_name, item in loaded_room_items.items():
                        if room_name in self.rooms:
                            self.rooms[room_name].item = item
            elif command == "exit":
                print("Thanks for playing!")
                break
            else:
                print("Invalid command. Try 'go [direction]', 'get', 'inventory',")
                print("'find', 'checklist', 'save', 'load', or 'exit'.")


# Start the game if the script is run directly
if __name__ == "__main__":
    game = Game()
    game.start()
