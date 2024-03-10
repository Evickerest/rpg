# pylint: disable=too-many-instance-attributes
"""Module for the CombatRoom class.
"""

import random
import csv
from Classes.Rooms.room import Room
from Classes.character import Enemy


class CombatRoom(Room):
    """Specialized Room that contains the generic non-boss enemy encounters.
    Attributes:
        ENEMIES (list): Contains the names of all potential enemies
    """

    ENEMIES = []

    @staticmethod
    def load_enemies() -> None:
        """Static method to load the different types of items from a specified file.
        """
        if not CombatRoom.ENEMIES:
            with open('Names/enemy_txt/monster_names', 'r',encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    CombatRoom.ENEMIES.append(row)

    def __init__(self):
        """Creates the CombatRoom instance.
        Args:
            *args: Currently nonfunctional. Meant to take an optional Player instance
             and scale enemies in room to said Player's level.
        """
        super().__init__()
        if not CombatRoom.ENEMIES:
            CombatRoom.load_enemies()
        self.player = None
        # if isinstance(args, Player):
        #     self.player = args
        #     self.mon_lv = self.player.stats["Level"]
        # else:

        self.mon_lv = 1
        self.enemies = []
        self.generate_enemies()
        self.name = self.generate_name("Combat")
        self.room_type = "Combat"
        self.text = "You have entered a Combat room. Prepare to fight."
        self.is_boss_room = False
        self.enemies_killed = 0

    def generate_enemies(self):
        """Method to fill the room with a random number of enemies.
        """
        num = random.randint(1, 4)
        if self.player:
            self.mon_lv = self.player.stats["Level"]
        for _ in range(0, num):
            mon_name = random.choice(CombatRoom.ENEMIES)
            self.enemies.append(Enemy(mon_name[0], None, self.mon_lv))

    def lv_enemies(self):
        """Method to level up enemies to match the Player instance associated
         with the Combat Room.
         """
        for enemy in self.enemies:
            if self.player:
                enemy.stats["Level"] = self.player.stats["Level"]
                enemy.stats["Stat Points"] = (self.player.stats["Level"] - 1) * 5
                enemy.update_stats()
