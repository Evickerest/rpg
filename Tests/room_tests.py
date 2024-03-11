"""Module containing the unittests for the Room class.
"""
import unittest
from Classes.Rooms.room import Room


class RoomTests(unittest.TestCase):
    """Testcase for the Room class.
    """
    def test_1make_room(self):
        """Test for the Room initialization.
        """
        x = Room()
        self.assertTrue(isinstance(x, Room))

    def test_2room_stats(self):
        """Test for the Room attributes.
        """
        x = Room()
        self.assertEqual(x.adjacent_rooms, [])
        self.assertEqual(x.is_currently_entered, False)
        self.assertEqual(x.has_entered, False)
        self.assertEqual(x.cleared, False)
        self.assertEqual(x.name, None)
        self.assertEqual(x.edges, [])
        self.assertEqual(x.pos_x, None)
        self.assertEqual(x.pos_y, None)

    def test_3set_coordinates(self):
        """Test for the set_coordinates method.
        """
        x = Room()
        self.assertEqual(x.pos_x, None)
        self.assertEqual(x.pos_y, None)
        x.set_coordinates(50, 88)
        self.assertEqual(x.pos_x, 50)
        self.assertEqual(x.pos_y, 88)

    def test_4get_coordinates(self):
        """Test for the get_coordinates method.
        """
        x = Room()
        self.assertEqual(x.get_coordinates(), [None, None])
        x.set_coordinates(50, 88)
        self.assertEqual(x.get_coordinates(), [50, 88])

    def test_5clear_room(self):
        """Test for the clear_room method.
        """
        x = Room()
        x.clear_room(True)
        self.assertTrue(x.cleared)

    def test_6get_cleared(self):
        """Test for the get_cleared method.
        """
        x = Room()
        self.assertFalse(x.get_cleared())

    def test_7create_adjacency(self):
        """Test for the create_adjacency method.
        """
        x = Room()
        y = Room()
        x.create_adjacency(y)
        self.assertTrue(y in x.adjacent_rooms)
        self.assertTrue(x in y.adjacent_rooms)

    def test_8create_adjacency_alreadyadjacent(self):
        """Test for the create_adjacency method if the rooms
         are already adjacent.
        """
        x = Room()
        y = Room()
        x.create_adjacency(y)
        y.create_adjacency(x)
        self.assertEqual(x.adjacent_rooms.count(y), 1)
        self.assertEqual(y.adjacent_rooms.count(x), 1)

    def test_9add_adjacent_room(self):
        """Test for the add_adjacent_room method.
        """
        x = Room()
        y = Room()
        x.add_adjacent_room(y)
        self.assertTrue(y in x.adjacent_rooms)
        self.assertFalse(x in y.adjacent_rooms)

    def test_10get_adjacent_rooms(self):
        """Test for the get_adjacent_rooms method.
        """
        x = Room()
        y = Room()
        self.assertEqual(x.get_adjacent_rooms(), [])
        self.assertEqual(y.get_adjacent_rooms(), [])
        x.create_adjacency(y)
        self.assertEqual(x.get_adjacent_rooms(), [y])
        self.assertEqual(y.get_adjacent_rooms(), [x])

    def test_11generate_name(self):
        """Test for the generate_name method.
        """
        x = Room()
        self.assertTrue(x.generate_name("Combat"))
        x = Room()
        self.assertTrue(x.generate_name("Shop"))
        x = Room()
        self.assertTrue(x.generate_name("Chest"))

    def test_12__repr__(self):
        """Test for the __repr__ method.
        """
        x = Room()
        x_name = x.generate_name("Combat")
        self.assertEqual(x.__repr__(), x_name)

    def test_13__eq__(self):
        """Test for the __eq__ method.
        """
        x = Room()
        y = Room()
        self.assertTrue(x.__eq__(y))
        x.set_coordinates(5, 1)
        self.assertFalse(x.__eq__(y))
