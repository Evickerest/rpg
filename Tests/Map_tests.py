import unittest
from Classes.Map.Map import *


class Map_tests(unittest.TestCase):
    def test1(self):
        map = Map()
        self.assertIsInstance(map, Map, "Map not valid object")