from Classes.Rooms.CombatRoom import CombatRoom
from Classes.Rooms.Room import Room
from Classes.Character import *

class BossRoom(Room):
    def __init__(self):
        super().__init__()
        self.name = self.generateName("Combat")
        self.roomType = "Boss"

        # mon_name = random.choice(CombatRoom.ENEMIES)
        mon_name = "BOSS"
        
        self.isBossRoom = True
        self.enemies = [Enemy(mon_name, None, 10)]


    