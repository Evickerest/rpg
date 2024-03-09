import unittest
from Classes.Rooms.StartRoom import *


class StartRoomTests(unittest.TestCase):

    def test_1make_startroom(self):
        x = StartRoom()
        self.assertTrue(isinstance(x, StartRoom))

    def test_2startroom_stats(self):
        x = StartRoom()
        self.assertEqual(x.roomType, "Start")
        self.assertEqual(x.name, "Start")
        self.assertEqual(x.text, "You are in the start room.")