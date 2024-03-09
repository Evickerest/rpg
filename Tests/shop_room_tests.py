"""Module containing the unittests for the ShopRoom class.
"""
import unittest
from Classes.Rooms.shop_room import ShopRoom


class ShopRoomTests(unittest.TestCase):
    """Testcase for the ShopRoom class.
    """
    def test_1make_shoproom(self):
        """Test for the ShopRoom initialization.
        """
        x = ShopRoom()
        self.assertTrue(isinstance(x, ShopRoom))

    def test_2shoproom_stats(self):
        """Test for the ShopRoom attributes.
        """
        x = ShopRoom()
        self.assertEqual(x.room_type, "Shop")
        self.assertTrue(x.name)
        self.assertEqual(x.text, "You have entered a Shop room. Prepare to buy items.")
        self.assertTrue(x.items)
        self.assertTrue(1 <= len(x.items) <= 4)
