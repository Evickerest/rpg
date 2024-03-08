import random

from Classes.Rooms.Room import Room
from Classes.Character import *
import csv


class CombatRoom(Room):

    ENEMIES = []

    @staticmethod
    def load_enemies() -> None:
        """Static method to load the different types of items from a specified file.
        """
        if not CombatRoom.ENEMIES:
            with open('Names/enemy_txt/monster_names', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    CombatRoom.ENEMIES.append(row)

    def __init__(self, *args):
        super().__init__()
        if not CombatRoom.ENEMIES:
            CombatRoom.load_enemies()
        self.player = None
        if isinstance(args, Player):
            self.player = args
            self.mon_lv = self.player.stats["Level"]
        else:
            self.mon_lv = 1
        self.enemies = []
        self.generate_enemies()
        self.name = self.generateName("Combat")
        self.roomType = "Combat"
        self.text = "You have entered a Combat room. Prepare to fight."
        self.isBossRoom = False

    def generate_enemies(self):
        num = random.randint(1, 4)
        if self.player:
            self.mon_lv = self.player.stats["Level"]
        for i in range(0, num):
            mon_name = random.choice(CombatRoom.ENEMIES)
            self.enemies.append(Enemy(mon_name[0], None, self.mon_lv))
