import random
import csv


class Item:

    ITEMS = []

    @staticmethod
    def load_items() -> None:
        """Static method to load the different types of items from a specified file.
        """
        if not Item.ITEMS:
            with open('Names/items_txt/item_types', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    Item.ITEMS.append(row)

    # Stats is a dictionary
    def __init__(self, stats: list):
        if not Item.ITEMS:
            Item.load_items()

        self.stats = {}
        self.stats["type"] = stats[0]
        self.stats["name"] = stats[1]
        self.stats["damage"] = int(stats[2])
        self.stats["defense"] = int(stats[3])
        self.stats["value"] = int(stats[4])
        self.stats["damagePercent"] = float(stats[5])
        self.stats["critPercent"] = 0.1
        self.stats["armorBreakPercent"] = 0.1
        self.assignStats()

        # self.assignStats() --> Testing, not using
        # Got to assign equipment's type
        # ["Weapon", "Head", "Arms", "Chest", "Legs", "Feet"]

    def assignStats(self):
        self.name = self.stats["name"]
        self.damage = self.stats["damage"]

        # What % Higher or % Lower from self.damage can possible damages be
        self.damagePercent = self.stats["damagePercent"]

        # In the format 0.%%
        self.critPercent = self.stats["critPercent"]

        # Chance of damage bypassing enemies defense
        self.armorBreakPercent = self.stats["armorBreakPercent"]

        ###### More stats can be added but idk

    # Enemy would be an instance of the enemy class
    def getDamageDealt(self, enemy):
        damageRangeValue = random.uniform(1 - self.damagePercent, 1 + self.damagePercent)
        baseDamageDealt = self.damage * damageRangeValue

        appliedDamage = baseDamageDealt
        if random.random() < self.critPercent:
            appliedDamage *= 2

        # If crit is 
        enemyDefenseReducer = 1
        if random.random() < self.armorBreakPercent:
            enemyDefenseReducer = 0.5

        enemyDefense = enemy.get_defense()

        return appliedDamage - enemyDefense * enemyDefenseReducer
