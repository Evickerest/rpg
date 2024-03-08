import unittest
from Classes.Rooms.Room import *


class RoomTests(unittest.TestCase):

    def test_1make_room(self):
        x = Room()
        self.assertTrue(isinstance(x, Room))

    def test_2room_stats(self):
        x = Room()
        self.assertEqual(x.adjacentRooms, [])
        self.assertEqual(x.isCurrentlyEntered, False)
        self.assertEqual(x.hasEntered, False)
        self.assertEqual(x.cleared, False)
        self.assertEqual(x.name, None)
        self.assertEqual(x.edges, [])
        self.assertEqual(x.posX, None)
        self.assertEqual(x.posY, None)

    def test_3setCoordinates(self):
        x = Room()
        self.assertEqual(x.posX, None)
        self.assertEqual(x.posY, None)
        x.setCoordinates(50, 88)
        self.assertEqual(x.posX, 50)
        self.assertEqual(x.posY, 88)

    def test_4getCoordinates(self):
        x = Room()
        self.assertEqual(x.getCoordinates(), [None, None])
        x.setCoordinates(50, 88)
        self.assertEqual(x.getCoordinates(), [50, 88])

    def test_5clearRoom(self):
        x = Room()
        x.clearRoom(True)
        self.assertTrue(x.cleared)

    def test_6getCleared(self):
        x = Room()
        self.assertFalse(x.getCleared())

    def test_7createAdjacency(self):
        x = Room()
        y = Room()
        x.createAdjacency(y)
        self.assertTrue(y in x.adjacentRooms)
        self.assertTrue(x in y.adjacentRooms)

    def test_8createAdjacency_AlreadyAdjacent(self):
        x = Room()
        y = Room()
        x.createAdjacency(y)
        y.createAdjacency(x)
        self.assertEqual(x.adjacentRooms.count(y), 1)
        self.assertEqual(y.adjacentRooms.count(x), 1)

    def test_9AddAdjacentRoom(self):
        x = Room()
        y = Room()
        x.addAdjacentRoom(y)
        self.assertTrue(y in x.adjacentRooms)
        self.assertFalse(x in y.adjacentRooms)

    def test_10getAdjacentRooms(self):
        x = Room()
        y = Room()
        self.assertEqual(x.getAdjacentRooms(), [])
        self.assertEqual(y.getAdjacentRooms(), [])
        x.createAdjacency(y)
        self.assertEqual(x.getAdjacentRooms(), [y])
        self.assertEqual(y.getAdjacentRooms(), [x])

    def test_11generateName(self):
        x = Room()
        self.assertTrue(x.generateName("Combat"))
        x = Room()
        self.assertTrue(x.generateName("Shop"))
        x = Room()
        self.assertTrue(x.generateName("Chest"))

    def test_12__repr__(self):
        x = Room()
        x_name = x.generateName("Combat")
        self.assertEqual(x.__repr__(), x_name)

    def test_13__eq__(self):
        x = Room()
        y = Room()
        self.assertTrue(x.__eq__(y))
        x.setCoordinates(5, 1)
        self.assertFalse(x.__eq__(y))
