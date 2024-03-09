"""Module containing the unittests for the Edge class.
"""
import unittest
from Classes.Map.Edge import *
from Classes.Rooms.CombatRoom import *


class Edge_tests(unittest.TestCase):
    """Testcase for the Edge class.
    """
    def test1(self):
        """Test that the Edge instance is made correctly.
        """
        room1 = CombatRoom()
        room1.set_coordinates(5, 10)
        room2 = CombatRoom()
        room2.set_coordinates(10, 5)
        edge = Edge(room1, room2)
        self.assertIsInstance(edge, Edge)

    def test2(self):
        """Test for the get_weight method.
        """
        room1 = CombatRoom()
        room1.set_coordinates(5, 10)
        room2 = CombatRoom()
        room2.set_coordinates(10, 5)
        edge = Edge(room1, room2)
        self.assertTrue(edge.get_weight())

    def test3(self):
        """Test for the __repr__ method.
        """
        room1 = CombatRoom()
        room1.set_coordinates(5, 10)
        room2 = CombatRoom()
        room2.set_coordinates(10, 5)
        edge = Edge(room1, room2)
        x = edge.__repr__()
        self.assertEqual(x, f"{room1} <-> {room2} | {edge.weight}")