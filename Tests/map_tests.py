"""Module containing the unittests for the Map class.
"""
import unittest
from Classes.Map.map import Map


class MapTests(unittest.TestCase):
    """Testcase for the Map class.
    """
    def test1(self):
        """Test that the Map initializes correctly.
        """
        test_map = Map()
        self.assertIsInstance(test_map, Map, "Map not valid object")

    def test2(self):
        """Test that the get_current_room method works.
        """
        test_map = Map()
        self.assertTrue(test_map.get_current_room())
