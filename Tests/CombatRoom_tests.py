import unittest
from Classes.Rooms.CombatRoom import *
from Classes.Character import *


class CombatRoomTests(unittest.TestCase):
    def test_1make_combatroom_no_player(self):
        x = CombatRoom(None)
        self.assertTrue(isinstance(x, CombatRoom))
        self.assertEqual(x.player, None)

    def test_2make_combatroom_player(self):
        return
        character = Player("Bob", None)
        x = CombatRoom(Player("Bob", None))
        self.assertTrue(isinstance(x, CombatRoom))
        self.assertEqual(x.player, character)

    def test_3combatroom_stats_no_player(self):
        x = CombatRoom(None)
        self.assertEqual(x.roomType, "Combat")
        self.assertTrue(x.name)
        self.assertEqual(x.text, "You have entered a Combat room. Prepare to fight.")
        self.assertEqual(x.mon_lv, 1)
        self.assertTrue(x.enemies)

    def test_4combatroom_stats_player(self):
        return
        character = Character("Bob", None)
        character.stats["Level"] = 5
        x = CombatRoom(character)
        self.assertEqual(x.roomType, "Combat")
        self.assertTrue(x.name)
        self.assertEqual(x.text, "You have entered a Combat room. Prepare to fight.")
        self.assertEqual(x.mon_lv, 5)
        for enemy in x.enemies:
            self.assertEqual(enemy.stats["Level"], character.stats["Level"])

    def test_5generate_enemies_no_player(self):
        x = CombatRoom(None)
        self.assertTrue(x.enemies)
        for enemy in x.enemies:
            self.assertEqual(enemy.stats["Level"], 1)

    def test_6generate_enemies_player(self):
        return
        character = Character("Bob", None)
        character.stats["Level"] = 5
        x = CombatRoom(character)
        self.assertTrue(x.enemies)
        for enemy in x.enemies:
            self.assertEqual(enemy.stats["Level"], character.stats["Level"])

