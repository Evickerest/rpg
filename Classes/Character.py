import random


class Character:
    # Stats is a dict
    def __init__(self, name, stats={"Strength": 5, "Dexterity": 5, "Vitality": 5,
                                    "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5, "Credits": 0}):
        self.name = name
        self.inventory = []
        self.stats = stats
        self.stats["Max Health"] = 20 + (5 * (self.stats["Vitality"] + self.stats["Level"]))
        self.stats["Health"] = self.stats["Max Health"]

    # Add to the inventory an instance of an item
    def addItem(self, item):
        self.inventory.append( item )

    # Upgrade stats by stat and amount
    def upgradeStats(self, stat, amount):
        if self.stats["Stat Points"] > 0:
            self.stats[stat] += amount
            self.stats["Stat Points"] -= 1
            self.updateMaxHealth()

    # Levels up and adds unassigned stat points
    def lv_up(self):
        if self.stats["XP"] >= (self.stats["Level"] * 10):
            self.stats["Level"] += 1
            self.stats["XP"] -= self.stats["Level"] * 10
            self.stats["Stat Points"] += 5

    # Recalculates max health
    def updateMaxHealth(self):
        self.stats["Max Health"] = 20 + (5 * (self.stats["Vitality"] + self.stats["Level"]))
        if self.stats["Health"] > self.stats["Max Health"]:
            self.stats["Health"] = self.stats["Max Health"]


class Player(Character):
    def __init__(self, name: str, stats: dict):
        super().__init__(name, stats)
        self.stats["Medkits"] = 5

class Enemy(Character):
    def __init__(self, name: str, stats: dict):
        super().__init__(name, stats)
        while self.stats["XP"] > self.stats["Level"] * 10:
            self.lv_up()
            stat = random.choice(['Strength', 'Dexterity', 'Vitality', 'Intelligence'])
            self.upgradeStats(stat, 1)
