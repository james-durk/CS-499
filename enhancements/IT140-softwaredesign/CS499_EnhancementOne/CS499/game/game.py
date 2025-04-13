from room import Room
from player import Player

class Game:
    def __init__(self):
        """
        Initialize the game with rooms, a player, and the game loop.
        """
        self.rooms = self.create_rooms()
        self.player = Player("Diver", self.rooms["Dive Shop Lobby"])

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
        print("Type 'go [direction]' to move or 'get' to pick up an item.")

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
            elif command == "exit":
                print("Thanks for playing!")
                break
            else:
                print("Invalid command. Try 'go [direction]', 'get', 'inventory', or 'exit'.")


# Start the game if the script is run directly
if __name__ == "__main__":
    game = Game()
    game.start()
