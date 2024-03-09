import unittest
from Classes.Character import *

import random
from Classes.Item import *


class CharacterTests(unittest.TestCase):

    def test_1make_character(self):
        x = Character("Bob", None)
        self.assertTrue(isinstance(x, Character))

    def test_2character_stats(self):
        x = Character("Default", {"Strength": 5, "Dexterity": 5, "Vitality": 5,
                      "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5, "Credits": 0})
        self.assertEqual(x.stats["Strength"], 5)
        self.assertEqual(x.stats["Dexterity"], 5)
        self.assertEqual(x.stats["Vitality"], 5)
        self.assertEqual(x.stats["Intelligence"], 5)
        self.assertEqual(x.stats["Level"], 1)
        self.assertEqual(x.stats["XP"], 0)
        self.assertEqual(x.stats["Stat Points"], 5)
        self.assertEqual(x.stats["Credits"], 0)

    def test_3set_living(self):
        x = Character("Bob", None)
        x.setLiving(False)
        self.assertFalse(x.living)

    def test_4addItem(self):
        x = Character("Bob", None)
        Item.load_items()
        item = Item(random.choice(Item.ITEMS))
        self.assertFalse(x.inventory)
        x.addItem(item)
        self.assertTrue(x.inventory)

    def test_5dropItem(self):
        x = Character("Bob", None)
        Item.load_items()
        item = Item(random.choice(Item.ITEMS))
        self.assertFalse(x.inventory)
        x.addItem(item)
        x.dropItem(item)
        self.assertFalse(x.inventory)

    def test_6lv_up(self):
        x = Character("Bob", None)
        x.stats["XP"] += 11
        x.lv_up()
        self.assertEqual(x.stats["Level"], 2)

    def test_7updateMaxHealth(self):
        x = Character("Bob", None)
        x.stats["Health"] += 11
        x.updateMaxHealth()
        self.assertEqual(x.stats["Health"], x.stats["Max Health"])

    def test_8updateHealth(self):
        x = Character("Bob", None)
        x.updateHealth(100)
        self.assertEqual(x.stats["Health"], x.stats["Max Health"])

    def test_9getDefense(self):
        x = Character("Bob", None)
        self.assertEqual(x.getDefense(), 0)

    def test_10getAttack(self):
        x = Character("Bob", None)
        self.assertEqual(x.getAttack(), 0)

    def test_11defend_action(self):
        x = Character("Bob", None)
        x.defense = 10
        self.assertEqual(x.getDefense(), 10)
        x.defend_action()
        self.assertEqual(x.getDefense(), 15)


class PlayerTests(unittest.TestCase):
    def test_1make_player(self):
        x = Player("Bob", None)
        self.assertTrue(isinstance(x, Player))

    def test_2player_stats(self):
        x = Player("Default", {"Strength": 5, "Dexterity": 5, "Vitality": 5,
                   "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5, "Credits": 0})
        self.assertEqual(x.stats["Strength"], 5)
        self.assertEqual(x.stats["Dexterity"], 5)
        self.assertEqual(x.stats["Vitality"], 5)
        self.assertEqual(x.stats["Intelligence"], 5)
        self.assertEqual(x.stats["Level"], 1)
        self.assertEqual(x.stats["XP"], 0)
        self.assertEqual(x.stats["Stat Points"], 5)
        self.assertEqual(x.stats["Credits"], 0)

    def test3_equip_item_Real(self):
        player = Player("Bob", None)
        x = Item(random.choice(Item.ITEMS))
        while x.stats["type"] != "Weapon":
            x = Item(random.choice(Item.ITEMS))
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Weapon"], x)

        while x.stats["type"] != "Head":
            x = Item(random.choice(Item.ITEMS))
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Head"], x)

        while x.stats["type"] != "Arms":
            x = Item(random.choice(Item.ITEMS))
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Arms"], x)

        while x.stats["type"] != "Chest":
            x = Item(random.choice(Item.ITEMS))
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Chest"], x)

        while x.stats["type"] != "Legs":
            x = Item(random.choice(Item.ITEMS))
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Legs"], x)

        while x.stats["type"] != "Feet":
            x = Item(random.choice(Item.ITEMS))
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Feet"], x)

    def test4_equip_item_NoneItem(self):
        player = Player("Bob", None)
        x = Item(["Weapon", "None", 0, 0, 0, 0.8])
        player.equipment["Weapon"] = x
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Weapon"], x)

        x = Item(["Head", "None", 0, 0, 0, 0.8])
        player.equipment["Head"] = x
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Head"], x)

        x = Item(["Chest", "None", 0, 0, 0, 0.8])
        player.equipment["Chest"] = x
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Chest"], x)

        x = Item(["Arms", "None", 0, 0, 0, 0.8])
        player.equipment["Arms"] = x
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Arms"], x)

        x = Item(["Legs", "None", 0, 0, 0, 0.8])
        player.equipment["Legs"] = x
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Legs"], x)

        x = Item(["Feet", "None", 0, 0, 0, 0.8])
        player.equipment["Feet"] = x
        player.addItem(x)
        player.equipItem(x)
        self.assertEqual(player.equipment["Feet"], x)

    def test_5unequipItem_Real(self):
        player = Player("Bob", None)
        x = player.equipment["Weapon"]
        player.unequipItem(x)
        unequipped = None
        for item in player.inventory:
            if item == x:
                unequipped = item
        self.assertEqual(x, unequipped)

        x = player.equipment["Head"]
        player.unequipItem(x)
        unequipped = None
        for item in player.inventory:
            if item == x:
                unequipped = item
        self.assertEqual(x, unequipped)

        x = player.equipment["Arms"]
        player.unequipItem(x)
        unequipped = None
        for item in player.inventory:
            if item == x:
                unequipped = item
        self.assertEqual(x, unequipped)

        x = player.equipment["Chest"]
        player.unequipItem(x)
        unequipped = None
        for item in player.inventory:
            if item == x:
                unequipped = item
        self.assertEqual(x, unequipped)

        x = player.equipment["Legs"]
        player.unequipItem(x)
        unequipped = None
        for item in player.inventory:
            if item == x:
                unequipped = item
        self.assertEqual(x, unequipped)

        x = player.equipment["Feet"]
        player.unequipItem(x)
        unequipped = None
        for item in player.inventory:
            if item == x:
                unequipped = item
        self.assertEqual(x, unequipped)

    def test_6unequipItem_None(self):
        player = Player("Bob", None)
        x = Item(["Weapon", "None", 0, 0, 0, 0.8])
        player.equipment["Weapon"] = x
        player.equipItem(x)
        player.unequipItem(x)
        self.assertEqual(player.inventory, [])

        x = Item(["Head", "None", 0, 0, 0, 0.8])
        player.equipment["Head"] = x
        player.equipItem(x)
        player.unequipItem(x)
        self.assertFalse(player.inventory)

        x = Item(["Chest", "None", 0, 0, 0, 0.8])
        player.equipment["Chest"] = x
        player.equipItem(x)
        player.unequipItem(x)
        self.assertFalse(player.inventory)

        x = Item(["Arms", "None", 0, 0, 0, 0.8])
        player.equipment["Arms"] = x
        player.equipItem(x)
        player.unequipItem(x)
        self.assertFalse(player.inventory)

        x = Item(["Legs", "None", 0, 0, 0, 0.8])
        player.equipment["Legs"] = x
        player.equipItem(x)
        player.unequipItem(x)
        self.assertFalse(player.inventory)

        x = Item(["Feet", "None", 0, 0, 0, 0.8])
        player.equipment["Feet"] = x
        player.equipItem(x)
        player.unequipItem(x)
        self.assertFalse(player.inventory)

    def test_7use_medkits(self):
        player = Player("Bob", None)
        player.use_medkits()
        self.assertEqual(player.stats["Medkits"], 4)
        player.stats["Health"] = 1
        player.use_medkits()
        self.assertTrue(player.stats["Health"] > 1)
        player.stats["Medkits"] = 0
        player.use_medkits()
        self.assertEqual(player.stats["Medkits"], 0)

    def test_8get_medkits(self):
        player = Player("Bob", None)
        self.assertEqual(player.med_kits, 5)

    def test_9set_medkits(self):
        player = Player("Bob", None)
        player.med_kits = -1
        self.assertEqual(player.med_kits, 4)

        player.med_kits = -100
        self.assertEqual(player.med_kits, 0)

    def test_10changeName(self):
        player = Player("Bob", None)
        player.changeName("SD")
        self.assertEqual(player.name, "SD")

    def test_11updateDefense(self):
        player = Player("Bob", None)
        defense = player.getDefense()
        player.stats["Vitality"] += 5
        player.updateDefense()
        self.assertTrue(player.getDefense() > defense)

    def test_12updateAttack(self):
        player = Player("Bob", None)
        attack = player.getAttack()
        player.stats["Strength"] += 5
        player.updateAttack()
        self.assertTrue(player.getAttack() > attack)

    def test_13takeDamage(self):
        player = Player("Bob", None)
        health = player.stats["Health"]
        player.take_damage(player)
        self.assertTrue(player.stats["Health"] < health)


class EnemyTests(unittest.TestCase):
    def test_1make_enemy(self):
        enemy = Enemy("Bob", None, 10)
        self.assertTrue(isinstance(enemy, Enemy))

    def test_2enemy_stats(self):
        enemy = Enemy("Bob", None, 10)
        self.assertEqual(enemy.stats["Level"], 10)
        self.assertEqual(enemy.name, "Bob")

    def test_3take_damage(self):
        enemy = Enemy("Bob", None, 10)
        player = Player("Ded", None)
        health = enemy.stats["Health"]
        enemy.take_damage(player)
        self.assertTrue(enemy.stats["Health"] < health)

        player.unequipItem(player.equipment["Weapon"])
        player.damage = 0
        enemy.take_damage(player)
        self.assertTrue(enemy.stats["Health"] < health)

    def test_4updateDefense(self):
        enemy = Enemy("Bob", None, 10)
        defense = enemy.getDefense()
        enemy.stats["Vitality"] += 10
        enemy.updateDefense()
        self.assertTrue(enemy.getDefense() > defense)

    def test_5updateAttack(self):
        enemy = Enemy("Bob", None, 10)
        attack = enemy.getAttack()
        enemy.stats["Strength"] += 10
        enemy.updateAttack()
        self.assertTrue(enemy.getAttack() > attack)

    def test_6updateStats(self):
        enemy = Enemy("Bob", None, 1)
        stat_sum = (enemy.stats["Strength"] + enemy.stats["Dexterity"] +
                    enemy.stats["Vitality"] + enemy.stats["Intelligence"])
        enemy.stats["Stat Points"] += 10
        enemy.updateStats()
        final_stat_sum = (enemy.stats["Strength"] + enemy.stats["Dexterity"] +
                          enemy.stats["Vitality"] + enemy.stats["Intelligence"])
        self.assertTrue(final_stat_sum > stat_sum)
