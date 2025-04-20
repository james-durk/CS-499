import sqlite3
import os
import json


class SaveManager:
    def __init__(self, db_name="game_save.db"):
        """
        Initializes the SaveManager with a database name and sets up the database schema if it doesn't exist.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the 'saves' table in the SQLite database if it doesn't already exist.
        This table stores the current room, inventory, and room-specific item states in JSON format.
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saves (
                id INTEGER PRIMARY KEY,
                current_room TEXT NOT NULL,
                inventory TEXT NOT NULL,
                room_items TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def save_game(self, current_room, inventory, rooms):
        """
        Saves the current game state to the database.

        Parameters:
            - current_room (str): The name of the room the player is currently in.
            - inventory (set): The player’s inventory as a set of item names.
            - rooms (dict): A dictionary mapping room names to Room objects, used to capture current room item states.
        """
        inventory_str = ",".join(inventory)

        # Create a dictionary of room items to store
        room_items = {room_name: room.item for room_name, room in rooms.items()}
        room_items_str = json.dumps(room_items)  # Convert to JSON string

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM saves")
        cursor.execute(
            "INSERT INTO saves (current_room, inventory, room_items) VALUES (?, ?, ?)",
            (current_room, inventory_str, room_items_str)
        )
        conn.commit()
        conn.close()
        print("Game saved successfully.")

    def load_game(self):
        """
        Loads the game state from the database.

        Returns:
            - current_room (str): The saved current room name.
             - inventory (set): The player's saved inventory as a set of item names.
            - room_items (dict): A mapping of room names to items currently present in each room.
        """
        if not os.path.exists(self.db_name):
            print("No save file found.")
            return None, None, None

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT current_room, inventory, room_items FROM saves LIMIT 1")
        result = cursor.fetchone()
        conn.close()

        if result:
            room, inventory_str, room_items_str = result
            inventory = set(inventory_str.split(",")) if inventory_str else set()
            room_items = json.loads(room_items_str)
            print("Game loaded successfully.")
            return room, inventory, room_items
        else:
            print("No saved game found.")
            return None, None, None


