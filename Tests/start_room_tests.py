"""Module containing the unittests for the StartRoom class.
"""
import unittest
from Classes.Rooms.start_room import StartRoom


class StartRoomTests(unittest.TestCase):
    """Testcase for the StartRoom class.
    """
    def test_1make_startroom(self):
        """Test for the StartRoom initialization.
        """
        x = StartRoom()
        self.assertTrue(isinstance(x, StartRoom))

    def test_2startroom_stats(self):
        """Test for the StartRoom instance variables.
        """
        x = StartRoom()
        self.assertEqual(x.room_type, "Start")
        self.assertEqual(x.name, "Start")
        self.assertEqual(x.text, "You are in the start room.")
