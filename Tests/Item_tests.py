# test Item class
import random
import unittest
from Classes.Item import *
from Classes.Character import *


class ItemTests(unittest.TestCase):

    def test_1load_items1(self):
        # Item list is not an empty list
        self.assertNotEquals(Item.ITEMS, [])

    def test_2load_items2(self):
        # Item list should exist
        self.assertTrue(Item.ITEMS)

    def test_3load_items3(self):
        # Item list has items
        Item.load_items()
        self.assertTrue(Item.ITEMS)

    def test_4load_items4(self):
        # Item list doesn't duplicate
        Item.load_items()
        x = len(Item.ITEMS)
        self.assertEqual(len(Item.ITEMS), x)
        Item.load_items()
        self.assertEqual(len(Item.ITEMS), x)

    def test_5make_item1(self):
        x = None
        Item.load_items()
        self.assertFalse(x)
        x = Item(random.choice(Item.ITEMS))
        self.assertTrue(x)
        self.assertTrue(isinstance(x, Item))

    def test_6item_stats1(self):
        Item.load_items()
        stats = random.choice(Item.ITEMS)
        x = Item(stats)
        type = stats[0]
        name = stats[1]
        damage = int(stats[2])
        defense = int(stats[3])
        value = int(stats[4])
        damagepercent = float(stats[5])
        self.assertEqual(x.stats["type"], type)
        self.assertEqual(x.stats["name"], name)
        self.assertEqual(x.stats["damage"], damage)
        self.assertEqual(x.stats["defense"], defense)
        self.assertEqual(x.stats["value"], value)
        self.assertEqual(x.stats["damagePercent"], damagepercent)

    def test_7item_assign_stats(self):
        Item.load_items()
        stats = random.choice(Item.ITEMS)
        x = Item(stats)
        x.assignStats()
        self.assertEqual(x.stats["name"], x.name)
        self.assertEqual(x.stats["damage"], x.damage)
        self.assertEqual(x.stats["armorBreakPercent"], x.armorBreakPercent)
        self.assertEqual(x.stats["critPercent"], x.critPercent)
        self.assertEqual(x.stats["damagePercent"], x.damagePercent)

    def test_8item_getDamage(self):
        Item.load_items()
        stats = random.choice(Item.ITEMS)
        x = Item(stats)
        enemy = Enemy("Tester", None, 1)
        self.assertTrue(x.getDamageDealt(enemy))

    def test_9item_notitem(self):
        stats = random.choice(Item.ITEMS)
        x = Item(stats)
        Item.load_items()
        self.assertTrue(Item.ITEMS, Item.ITEMS)
