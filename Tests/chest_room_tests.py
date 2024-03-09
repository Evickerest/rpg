"""Module containing the unittests for ChestRoom.
"""
import unittest
from Classes.Rooms.chest_room import ChestRoom


class ChestRoomTests(unittest.TestCase):
    """Testcase for ChestRoom.
    """

    def test_1make_chestroom(self):
        """Test that the instance is made correctly.
        """
        x = ChestRoom()
        self.assertTrue(isinstance(x, ChestRoom))

    def test_2chestroom_stats(self):
        """Test to check for specific instance attributes.
        """
        x = ChestRoom()
        self.assertEqual(x.room_type, "Chest")
        self.assertTrue(x.name)
        self.assertEqual(x.text, "You have entered a Chest room. Prepare to open a chest.")
