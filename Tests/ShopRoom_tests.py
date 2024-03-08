import unittest
from Classes.Rooms.ShopRoom import *
from Classes.Character import *


class ShopRoomTests(unittest.TestCase):
    def test_1make_shoproom(self):
        x = ShopRoom()
        self.assertTrue(isinstance(x, ShopRoom))

    def test_2shoproom_stats(self):
        x = ShopRoom()
        self.assertEqual(x.roomType, "Shop")
        self.assertTrue(x.name)
        self.assertEqual(x.text, "You have entered a Shop room. Prepare to buy items.")
        self.assertTrue(x.items)
        self.assertTrue(1 <= len(x.items) <= 4)