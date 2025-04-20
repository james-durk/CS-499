class Player:
    def __init__(self, name, starting_room, inventory=None):
        """
        Initialize a Player object with a name, starting room, and an empty inventory.
        """
        self.name = name
        self.current_room = starting_room
        self.inventory = set(inventory) if inventory else set()  # Using a set for quick lookups

    def move(self, direction):
        """
        Move the player to a connected room if possible.
        """
        next_room = self.current_room.get_connection(direction)
        if next_room:
            self.current_room = next_room
            print(f"You moved to {self.current_room.name}")
        else:
            print("You can't go that way.")

    def pick_up_item(self):
        """
        Pick up an item from the current room if available.
        """
        if self.current_room.has_item():
            item = self.current_room.take_item()
            self.inventory.add(item)
            print(f"You picked up: {item}")
        else:
            print("There's nothing to pick up here.")

    def show_inventory(self):
        """
        Display the player's inventory.
        """
        if self.inventory:
            print("Your inventory contains:", ", ".join(self.inventory))
        else:
            print("Your inventory is empty.")
