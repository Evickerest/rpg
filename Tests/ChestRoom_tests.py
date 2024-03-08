import unittest
from Classes.Rooms.ChestRoom import *


class ChestRoomTests(unittest.TestCase):

    def test_1make_chestroom(self):
        x = ChestRoom()
        self.assertTrue(isinstance(x, ChestRoom))

    def test_2chestroom_stats(self):
        x = ChestRoom()
        self.assertEqual(x.roomType, "Chest")
        self.assertTrue(x.name)
        self.assertEqual(x.text, "You have entered a Chest room. Prepare to open a chest.")
