"""Module for the ChestRoom class.
"""

from Classes.Rooms.Room import Room
from Classes.Item import *


class ChestRoom(Room):
    """A specialzed Room that contains an item.
    """
    def __init__(self):
        """Creates the instance.
        """
        super().__init__()
        self.name = self.generate_name("Chest")
        self.room_type = "Chest"
        self.item = Item(random.choice(Item.ITEMS))

        self.text = "You have entered a Chest room. Prepare to open a chest."
