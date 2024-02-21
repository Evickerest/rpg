from Classes.Rooms.Room import Room


class CombatRoom(Room):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.name = self.generateName("Combat")
        self.roomType = "Combat"
        self.text = "You have entered a Combat room. Prepare to fight."

   
