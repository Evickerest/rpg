import csv
from Classes.Rooms.Room import Room


class ChestRoom(Room):
    def __init__(self):
        super().__init__()
        self.name = self.generateName("Chest")
        self.roomType = "Chest"

        self.text = "You have entered a Chest room. Prepare to open a chest."

        
        
