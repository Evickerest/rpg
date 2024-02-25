import csv
from Classes.Rooms.Room import Room
from Classes.Item import *


class ShopRoom(Room):
    def __init__(self):
        super().__init__()
        self.name = self.generateName("Shop")
        self.roomType = "Shop"
        self.items = []

        num_items = random.randint(1, 4)
        for i in range(1, num_items):
            self.items.append(Item(random.choice(Item.ITEMS)))

        self.text = "You have entered a Shop room. Prepare to buy items."
