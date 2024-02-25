import random

from Classes.Item import *

if not Item.ITEMS:
    Item.load_items()


class Character:
    # Stats is a dict
    def __init__(self, name, stats=None):
        if stats is None:
            stats = {"Strength": 5, "Dexterity": 5, "Vitality": 5,
                     "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5, "Credits": 0}
        self.name = name
        self.inventory = []
        self.stats = stats
        self.stats["Max Health"] = 20 + (5 * (self.stats["Vitality"] + self.stats["Level"]))
        self.stats["Health"] = self.stats["Max Health"]
        self.attack = 0  # Pull item attack + character strength?
        self.defense = 0  # Pull item defense + character vitality?
        self.living = True

    # Set's character's living status
    def setLiving(self, _bool):
        self.living = _bool

    # Add to the inventory an instance of an item
    def addItem(self, item: Item):
        self.inventory.append(item)

    def dropItem(self, item: Item):
        self.inventory.remove(item)

    # Upgrade stats by stat and amount
    def upgradeStats(self, stat, amount):
        if self.stats["Stat Points"] > 0:
            self.stats[stat] += amount
            self.stats["Stat Points"] -= amount
        if stat == "Vitality":
            self.updateMaxHealth()
            self.updateHealth(5 * amount)

    # Levels up and adds unassigned stat points
    def lv_up(self):
        if self.stats["XP"] >= (self.stats["Level"] * 10):
            self.stats["XP"] -= self.stats["Level"] * 10
            self.stats["Level"] += 1
            self.stats["Stat Points"] += 5

    # Recalculates max health
    def updateMaxHealth(self):
        self.stats["Max Health"] = 20 + (5 * (self.stats["Vitality"] + self.stats["Level"]))
        if self.stats["Health"] > self.stats["Max Health"]:
            self.stats["Health"] = self.stats["Max Health"]

    def updateHealth(self, amount: int):
        self.stats["Health"] += amount
        if self.stats["Health"] > self.stats["Max Health"]:
            self.stats["Health"] = self.stats["Max Health"]

    def getDefense(self):
        return self.defense

    def getAttack(self):
        return self.attack

    def defend_action(self):
        self.defense = int(self.defense * 1.5)


class Player(Character):
    def __init__(self, name: str, stats: dict):
        super().__init__(name, stats)
        self.stats["Medkits"] = 5

        self.equipment = {}
        x = Item(random.choice(Item.ITEMS))
        while x.stats["type"] != "Weapon":
            x = Item(random.choice(Item.ITEMS))
        self.equipment["Weapon"] = x
        while x.stats["type"] != "Head":
            x = Item(random.choice(Item.ITEMS))
        self.equipment["Head"] = x
        while x.stats["type"] != "Arms":
            x = Item(random.choice(Item.ITEMS))
        self.equipment["Arms"] = x
        while x.stats["type"] != "Chest":
            x = Item(random.choice(Item.ITEMS))
        self.equipment["Chest"] = x
        while x.stats["type"] != "Legs":
            x = Item(random.choice(Item.ITEMS))
        self.equipment["Legs"] = x
        while x.stats["type"] != "Feet":
            x = Item(random.choice(Item.ITEMS))
        self.equipment["Feet"] = x
        self.updateAttack()
        self.updateDefense()

    def equipItem(self, item: Item):
        if item in self.inventory:
            if item.stats["type"] == "Weapon":
                if self.equipment["Weapon"].stats["name"] == "None":
                    self.equipment["Weapon"] = item
                else:
                    tmp = self.equipment["Weapon"]
                    self.equipment["Weapon"] = item
                    self.addItem(tmp)
            elif item.stats["type"] == "Head":
                if self.equipment["Head"].stats["name"] == "None":
                    self.equipment["Head"] = item
                else:
                    tmp = self.equipment["Head"]
                    self.equipment["Head"].stats["name"] = item
                    self.addItem(tmp)
            elif item.stats["type"] == "Arms":
                if self.equipment["Arms"].stats["name"] == "None":
                    self.equipment["Arms"] = item
                else:
                    tmp = self.equipment["Arms"]
                    self.equipment["Arms"] = item
                    self.addItem(tmp)
            elif item.stats["type"] == "Chest":
                if self.equipment["Chest"].stats["name"] == "None":
                    self.equipment["Chest"] = item
                else:
                    tmp = self.equipment["Chest"]
                    self.equipment["Chest"] = item
                    self.addItem(tmp)
            elif item.stats["type"] == "Legs":
                if self.equipment["Legs"].stats["name"] == "None":
                    self.equipment["Legs"] = item
                else:
                    tmp = self.equipment["Legs"]
                    self.equipment["Legs"] = item
                    self.addItem(tmp)
            elif item.stats["type"] == "Feet":
                if self.equipment["Feet"].stats["name"] == "None":
                    self.equipment["Feet"] = item
                else:
                    tmp = self.equipment["Feet"]
                    self.equipment["Feet"] = item
                    self.addItem(tmp)
            self.inventory.remove(item)
            self.updateAttack()
            self.updateDefense()

    def unequipItem(self, item: Item):
        if item.stats["type"] == "Weapon":
            if item.stats["name"] != "None":
                self.addItem(self.equipment["Weapon"])
            self.equipment["Weapon"] = Item(["Weapon", "None", 0, 0, 0, 0.8])
        elif item.stats["type"] == "Head":
            if item.stats["name"] != "None":
                self.addItem(self.equipment["Head"])
            self.equipment["Head"] = Item(["Head", "None", 0, 0, 0, 0.8])
        elif item.stats["type"] == "Arms":
            if item.stats["name"] != "None":
                self.addItem(self.equipment["Arms"])
            self.equipment["Arms"] = Item(["Arms", "None", 0, 0, 0, 0.8])
        elif item.stats["type"] == "Chest":
            if item.stats["name"] != "None":
                self.addItem(self.equipment["Chest"])
            self.equipment["Chest"] = Item(["Chest", "None", 0, 0, 0, 0.8])
        elif item.stats["type"] == "Legs":
            if item.stats["name"] != "None":
                self.addItem(self.equipment["Legs"])
            self.equipment["Legs"] = Item(["Legs", "None", 0, 0, 0, 0.8])
        elif item.stats["type"] == "Feet":
            if item.stats["name"] != "None":
                self.addItem(self.equipment["Feet"])
            self.equipment["Feet"] = Item(["Feet", "None", 0, 0, 0, 0.8])
        self.updateAttack()
        self.updateDefense()

    def use_medkits(self):
        if self.med_kits > 0:
            self.med_kits = -1
            amt = self.stats["Intelligence"] + self.stats["Level"] + 20
            tmp = self.stats["Health"] + amt
            if tmp >= self.stats["Max Health"]:
                amt = self.stats["Max Health"] - self.stats["Health"]
                self.stats["Health"] = self.stats["Max Health"]
            print(self.name + " used a med kit and healed " + str(amt) + " health.")
            return amt
        else:
            print("No med kits left.")
            return 0

    @property
    def med_kits(self) -> int:
        return self.stats["Medkits"]

    @med_kits.setter
    def med_kits(self, change: int):
        self.stats["Medkits"] += change
        if self.stats["Medkits"] < 0:
            self.__med_kits = 0

    def changeName(self, name):
        self.name = name

    def updateDefense(self):
        self.defense = int((self.stats["Vitality"] + self.stats["Level"]) / 5)
        for equipment in self.equipment.values():
            self.defense += equipment.stats["defense"]

    def updateAttack(self):
        self.attack = int((self.stats["Strength"] + self.stats["Level"]) / 5)
        for equipment in self.equipment.values():
            self.attack += equipment.stats["damage"]

    def take_damage(self, attacker: Character):
        damage = attacker.getAttack()
        self.stats["Health"] -= damage


class Enemy(Character):
    def __init__(self, name, stats: dict, enemy_lv: int):
        super().__init__(stats)
        self.stats["Level"] = enemy_lv
        self.name = name
        self.stats["Stat Points"] = self.stats["Level"] * 5
        while self.stats["Stat Points"] > 1:
            stat = random.choice(['Strength', 'Dexterity', 'Vitality', 'Intelligence'])
            self.upgradeStats(stat, 1)
        self.updateAttack()
        self.updateDefense()

    def take_damage(self, attacker: Player):
        item = attacker.equipment["Weapon"]
        damage = item.getDamageDealt(self) + attacker.getAttack()
        self.stats["Health"] -= damage

    def updateDefense(self):
        self.defense = int((self.stats["Vitality"] + self.stats["Level"]) / 5)

    def updateAttack(self):
        self.attack = int((self.stats["Strength"] + self.stats["Level"]) / 5)
