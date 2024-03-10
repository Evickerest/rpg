"""Module containing the unittests for CombatRoom.
"""

import unittest
from Classes.Rooms.combat_room import CombatRoom
from Classes.character import Player


class CombatRoomTests(unittest.TestCase):
    """Testcase for CombatRoom.
    """
    def test_1make_combatroom(self):
        """Check that the CombatRoom initializes.
        """
        x = CombatRoom()
        self.assertTrue(isinstance(x, CombatRoom))
        self.assertEqual(x.player, None)

    def test_2combatroom_stats(self):
        """Check that the CombatRoom's instance attributes are correct.
        """
        x = CombatRoom()
        self.assertEqual(x.room_type, "Combat")
        self.assertTrue(x.name)
        self.assertFalse(x.is_boss_room)
        self.assertEqual(x.mon_lv, 1)
        self.assertTrue(x.enemies)

    def test_3generate_enemies(self):
        """Check that the CombatRoom correctly generates enemies at LV 1.
        """
        x = CombatRoom()
        self.assertTrue(x.enemies)
        for enemy in x.enemies:
            self.assertEqual(enemy.stats["Level"], 1)

    def test_4lv_enemies(self):
        """Check that the CombatRoom correctly updates enemy levels.
        """
        x = CombatRoom()
        character = Player("Bob", None)
        character.stats["Level"] = 10
        x.player = character
        x.lv_enemies()
        for enemy in x.enemies:
            self.assertEqual(enemy.stats["Level"], x.player.stats["Level"])
