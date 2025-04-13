class Room:
    def __init__(self, name, description, item=None):
        """
        Initialize a Room object with a name, description, and optional item.
        """
        self.name = name
        self.description = description
        self.item = item
        self.connections = {}

    def set_connection(self, direction, room):
        """
        Define room connections for movement.
        """
        self.connections[direction] = room

    def get_connection(self, direction):
        """
        Return the room in the given direction, if it exists.
        """
        return self.connections.get(direction, None)

    def has_item(self):
        """
        Check if the room contains an item.
        """
        return self.item is not None

    def take_item(self):
        """
        Remove the item from the room when collected.
        """
        item = self.item
        self.item = None
        return item

    def __str__(self):
        """
        String representation of the room.
        """
        return f"{self.name}: {self.description}"
