import unittest
from Classes.Rooms.BossRoom import *


class BossRoomTests(unittest.TestCase):

    def test_1make_bossroom(self):
        x = BossRoom()
        self.assertTrue(isinstance(x, BossRoom))

    def test_2bossroom_stats(self):
        x = BossRoom()
        self.assertEqual(x.roomType, "Boss")
        self.assertTrue(x.name)
        self.assertTrue(x.isBossRoom)
        self.assertTrue(x.enemies)
        self.assertEqual(x.enemies[0].name, "BOSS")
