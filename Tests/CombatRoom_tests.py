import unittest
from Classes.Rooms.CombatRoom import *
from Classes.Character import *


class CombatRoomTests(unittest.TestCase):
    def test_1make_combatroom(self):
        x = CombatRoom()
        self.assertTrue(isinstance(x, CombatRoom))
        self.assertEqual(x.player, None)

    def test_2combatroom_stats(self):
        x = CombatRoom()
        self.assertEqual(x.roomType, "Combat")
        self.assertTrue(x.name)
        self.assertEqual(x.text, "You have entered a Combat room. Prepare to fight.")
        self.assertEqual(x.mon_lv, 1)
        self.assertTrue(x.enemies)

    def test_3generate_enemies(self):
        x = CombatRoom()
        self.assertTrue(x.enemies)
        for enemy in x.enemies:
            self.assertEqual(enemy.stats["Level"], 1)

    def test_4lv_enemies(self):
        x = CombatRoom()
        character = Player("Bob", None)
        character.stats["Level"] = 10
        x.player = character
        x.lv_enemies()
        for enemy in x.enemies:
            self.assertEqual(enemy.stats["Level"], x.player.stats["Level"])
