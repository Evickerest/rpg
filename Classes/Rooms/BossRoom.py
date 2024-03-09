"""Module for the BossRoom class.
"""

from Classes.Rooms.CombatRoom import CombatRoom
from Classes.Rooms.Room import Room
from Classes.Character import *


class BossRoom(Room):
    """Acts similarly to CombatRoom.
    """
    def __init__(self):
        """Creates the instance."""
        super().__init__()
        self.name = self.generate_name("Combat")
        self.room_type = "Boss"

        # mon_name = random.choice(CombatRoom.ENEMIES)
        mon_name = "BOSS"
        
        self.is_boss_room = True
        self.enemies = [Enemy(mon_name, None, 10)]
    