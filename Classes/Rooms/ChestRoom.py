import csv
from Classes.Rooms.Room import Room
from Classes.Item import *


class ChestRoom(Room):
    def __init__(self):
        super().__init__()
        self.name = self.generateName("Chest")
        self.roomType = "Chest"
        self.item = Item(random.choice(Item.ITEMS))

        self.text = "You have entered a Chest room. Prepare to open a chest."
