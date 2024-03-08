import unittest
from Classes.Map.Edge import *
from Classes.Rooms.CombatRoom import *


class Edge_tests(unittest.TestCase):
    def test1(self):
        room1 = CombatRoom()
        room1.setCoordinates(5, 10)
        room2 = CombatRoom()
        room2.setCoordinates(10, 5)
        edge = Edge(room1, room2)
        self.assertIsInstance(edge, Edge)

    def test2(self):
        room1 = CombatRoom()
        room1.setCoordinates(5, 10)
        room2 = CombatRoom()
        room2.setCoordinates(10, 5)
        edge = Edge(room1, room2)
        self.assertTrue(edge.getWeight())

    def test3(self):
        room1 = CombatRoom()
        room1.setCoordinates(5, 10)
        room2 = CombatRoom()
        room2.setCoordinates(10, 5)
        edge = Edge(room1, room2)
        x = edge.__repr__()
        self.assertEqual(x, f"{room1} <-> {room2} | {edge.weight}")