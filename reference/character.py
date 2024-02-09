"""Create player characters with different classes. Creates more generic
monsters as enemies.

Phuc Le
11/10/2023
Version 3.2
"""
import random
from random import *
from item import *
from datetime import *


class Character:
    """The base Character class containing from which the more specific
     player classes and Monster class is customized from.
    """
    def __init__(self, name: str) -> None:
        """The constructor for the Character instance.
        Args:
            name (str): The Character's name. Cannot be blank (Exception Handling)
        Except:
            ValueError: The character's name must be a non-empty string.
        """
        if not isinstance(name, str):
            raise ValueError("The character's name must be a string.")
        if not name:
            raise ValueError("The character's name cannot be an empty string.")

        self.__name = name
        self.__strength = 1
        self.__dexterity = 1
        self.__vitality = 1
        self.__intelligence = 1
        self.__level = 1
        self.__xp = 0
        self.__stats = 0
        self.__max_health = 50 + (5 * (self.vitality + self.level))
        self.__health = self.max_health
        self.base_attack = 0
        self.base_defense = 0
        self.__inventory: list[Item] = []
        self.__armor: list[Armor] = []
        self.__weapon = Weapon(["weapon", "barehanded", 0, 0, 0])
        self.__weapon.condition = ["Regular", 1.0]  # Need to change the 1.0 to "1.0"
        self.__inventory_weight = 0
        self.__max_weight = 5

    @property
    def name(self) -> str:
        """Getter for the __name attribute:
        Returns:
            self.__name (str): The name of a character.
        """
        return self.__name

    @property
    def max_health(self) -> int:
        """Getter for the __max_health attribute.
        Returns:
            __max_health (int): The max health of a character.
        """
        return self.__max_health

    @max_health.setter
    def max_health(self, change: int) -> None:
        """Setter for the __max_health attribute.
        Args:
            change (int): The change to a character's current max health amount.
            A positive value increases max health.
        Except:
            ValueError: change must be an integer.
            CharacterDeathException: If the character's max health hits or drops below 0.
        """
        if not isinstance(change, int):
            raise ValueError("The health change must be an integer.")
        self.__max_health = self.__max_health + change
        try:
            if self.__max_health <= 0:
                raise CharacterDeathException(self.name + "'s max health is <=0.", self)
        except CharacterDeathException:
            print(self.name + "'s health is <=0.", self)

    @property
    def health(self) -> int:
        """Getter for the __health attribute.
        Returns:
            __health (int): The current health of a character.
        """
        return self.__health

    @health.setter
    def health(self, change: int) -> None:
        """Setter for the __health attribute.
        Args:
            change (int): The change to a character's current health amount.
            A positive value increases health.
        Except:
            ValueError: change must be an integer.
            CharacterDeathException: If the character's health hits or drops below 0.
        """
        if not isinstance(change, int):
            raise ValueError("The health change must be an integer.")
        self.__health = self.__health + change
        try:
            if self.health <= 0:
                raise CharacterDeathException(self.name + "'s health is <=0.", self)
        except CharacterDeathException:
            print(self.name + "'s health is <=0.", self)

    @property
    def weapon(self) -> Weapon:
        """Getter for the __weapon attribute
        Returns:
            __weapon (Weapon): The weapon a character is wielding.
        """
        return self.__weapon

    @weapon.setter
    def weapon(self, weapon: Weapon) -> None:
        """Setter for the __weapon attribute.
        Args:
            weapon (Weapon): The new Weapon instance for the character to wield.
        Except:
            ValueError: The weapon argument must be a Weapon instance.
        """
        if not isinstance(weapon, Weapon):
            raise ValueError("The weapon passed in must be a Weapon instance.")
        self.__weapon = weapon

    @property
    def armor(self) -> list[Armor]:
        """Getter for the armor a character is wearing.
        Returns:
            __armor (list[Armor]): The list of armor pieces a character is wearing.
        """
        return self.__armor

    @armor.setter
    def armor(self, armor_name: Armor) -> None:
        """Setter that modified the __armor attribute.
        Args:
            armor_name (Armor): The Armor instance the character will wear.
        Except:
            ValueError: The armor_name passed in is not an Armor instance.
        """
        if not isinstance(armor_name, Armor):
            raise ValueError("The armor passed in wasn't an Armor instance.")
        for armor in self.__armor:
            if armor.description == armor_name.description:
                self.__armor.remove(armor_name)
                self.__inventory.append(armor_name)
        self.__armor.append(armor_name)

    @property
    def stats(self) -> int:
        """Getter for the character's unallocated stat points.
        Returns:
            __free_stats (int): The character's current unallocated stat points.
        """
        return self.__stats

    @stats.setter
    def stats(self, change: int):
        """Setter for the __stats attribute.
        Args:
            change (int): How much to change __stats by.
        """
        self.__stats += change
        if self.__stats < 0:
            self.__stats = 0

    @property
    def strength(self) -> int:
        """Getter for the character's strength.
        Returns:
            __strength (int): The character's current strength.
        """
        return self.__strength

    @strength.setter
    def strength(self, change: int):
        """Setter for the __strength attribute.
        Args:
            change (int): How much to change __strength by.
        """
        self.__strength += change
        if self.__strength < 0:
            self.__strength = 0

    @property
    def dexterity(self) -> int:
        """Getter for the character's dexterity.
            Returns:
                __dexterity (int): The character's current dexterity.
            """
        return self.__dexterity

    @dexterity.setter
    def dexterity(self, change: int):
        """Setter for the __dexterity attribute.
        Args:
            change (int): How much to change __dexterity by.
        """
        self.__dexterity += change
        if self.__dexterity < 0:
            self.__dexterity = 0

    @property
    def vitality(self) -> int:
        """Getter for the character's vitality.
        Returns:
            __vitality (int): The character's current vitality.
        """
        return self.__vitality

    @vitality.setter
    def vitality(self, change: int):
        """Setter for the __vitality attribute.
        Args:
            change (int): How much to change __vitality by.
        """
        self.__vitality += change
        if self.__vitality < 0:
            self.__vitality = 0

    @property
    def intelligence(self) -> int:
        """Getter for the character's intelligence.
        Returns:
            __intelligence (int): The character's current intelligence.
        """
        return self.__intelligence

    @intelligence.setter
    def intelligence(self, change: int):
        """Setter for the __intelligence attribute.
        Args:
            change (int): How much to change __intelligence by.
        """
        self.__intelligence += change
        if self.__intelligence < 0:
            self.__intelligence = 0

    @property
    def level(self) -> int:
        """Getter for the character's level.
        Returns:
            __level (int): The character's current level.
        """
        return self.__level

    @level.setter
    def level(self, change: int):
        """Setter for the __level attribute.
        Args:
            change (int): How much to change __level by.
        """
        self.__level += change

    @property
    def xp(self) -> int:
        """Getter for the character's __xp.
        Returns:
            __xp (int): The character's current __xp.
        """
        return self.__xp

    @xp.setter
    def xp(self, change: int):
        """Setter for the __xp attribute.
        Args:
            change (int): How much to change __xp by.
        """
        self.__xp += change

    def inventory(self) -> list[Item]:
        """Getter for the __inventory attribute.
        Returns:
            __inventory (list[Item]): The list of Items in a character's inventory.
        """
        return self.__inventory

    def in_inventory(self, item_description: str) -> Item | None:
        """Checks if the item is in the character's inventory or not.
        Args:
            item_description (str): The item description to search for.
        Returns:
            item (Item): The Item instance if it was found.
            None: If the Item instance wasn't found.
        Except:
            ValueError: The item_description wasn't a string.
            ValueError: The item_description must be a non-empty string.
        """
        if not isinstance(item_description, str):
            raise ValueError("The item's description wasn't a string.")
        if not item_description:
            raise ValueError("The item's description must be a non-empty string.")
        for item in self.inventory():
            if isinstance(item, Item):
                if item_description == item.description:
                    return item
            else:
                return None
        return None

    def add_inventory(self, item_name: Item) -> None:
        """Adds an Item instance to the character's inventory.
        Args:
            item_name (Item): The item to add to the inventory.
        Except:
            ValueError: The item_name passed in wasn't an Item instance.
        """
        if not isinstance(item_name, Item):
            raise ValueError("The item you wanted to add wasn't an Item instance.")
        self.__inventory.append(item_name)

    def wearing(self, item_description: str) -> Armor | None:
        """Determines if the item_description inputted was already worn or not.
        Args:
            item_description (str): The item's description to look up.
        Returns:
            armor (Armor): The Armor instance if you were wearing the specified armor.
            None: If you weren't wearing the specified armor piece.
        Except:
            ValueError: The item_description passed in wasn't a string.
            ValueError: The item's description was an empty string.
        """
        if not isinstance(item_description, str):
            raise ValueError("The item's description wasn't a string.")
        if not item_description:
            raise ValueError("The item's description can't be an empty string.")
        for armor in self.armor:
            if item_description == armor.description:
                return armor
        return None

    @property
    def base_attack(self) -> int:
        """Getter for the __base_attack attribute.
        Returns:
            __base_attack (int): A character's base attack.
        """
        return self.__base_attack

    @base_attack.setter
    def base_attack(self, *args) -> None:
        """Setter for the __base_attack attribute.
        """
        self.__base_attack = 4 + self.strength + self.level

    @property
    def base_defense(self) -> int:
        """Getter for the __base_defense attribute.
        Returns:
            __base_defense (int): A character's base defense.
        """
        return self.__base_defense

    @base_defense.setter
    def base_defense(self, *args) -> None:
        """Setter for the __base_defense attribute.
        """
        self.__base_defense = int(4 + self.vitality//2 + self.level*.5)

    @property
    def inventory_weight(self) -> int:
        """Calculates the weight of all items in a character's inventory
         and stores it as __inventory_weight.
        Returns:
            __inventory_weight (int): The weight a character is carrying.
        """
        self.__inventory_weight = 0
        for item in self.inventory():
            if isinstance(item, Item):
                self.__inventory_weight = self.__inventory_weight + item.weight
        return self.__inventory_weight

    @property
    def max_weight(self) -> int:
        """Getter for the __max_weight attribute.
        Returns:
            __max_weight (int): The maximum carry weight of a character.
        """
        return self.__max_weight

    def total_defense(self) -> int:
        """Calculates a character's total defense as a result of their
         base defense and all armor pieces worn.
        Returns:
            sum_defense (int): The total defense a character has.
        """
        sum_defense = self.__base_defense
        if not self.__armor:
            return sum_defense
        else:
            for armor in self.__armor:
                sum_defense = sum_defense + armor.added_defense
            return sum_defense

    def total_attack(self) -> int:
        """Calculates a character's total attack as a result of their
         base attack and the weapon they're wielding.
        Returns:
            sum_attack (int): The total attack a character has.
        """
        sum_attack = self.__base_attack + int(self.__weapon.added_attack)
        return sum_attack

    def take_damage(self, enemy: object) -> int:
        """Calculates the damage this character will take when attacked
         by the specified enemy.
        Args:
            enemy (object): Specifically, the Character instance that is attacking.
        Returns:
            damage (int): The damage this character will take expressed as a positive value.
        Except:
            ValueError: The enemy object passed in wasn't a Character instance.
        """
        if isinstance(enemy, Character):
            damage = enemy.total_attack() - self.total_defense()
            if randint(0, 100) == 100:
                damage = 2 * enemy.total_attack()
                print("Critical Hit! " + enemy.name + "'s attack ignored " + self.name + "'s defense.")
            if damage <= 0:
                return 0
            else:
                self.health = -damage
            return damage
        else:
            raise ValueError("The enemy object specified wasn't a Character instance.")

    def __str__(self) -> str:
        """String method containing all the information on a character.
        Returns:
            str: A long strong about a character's
             name, class, weapon, armor, inventory, and total stats.
        """
        self.__char_att = self.total_attack()
        self.__char_def = self.total_defense()
        self.__char_inv = []
        for item in self.inventory():
            if isinstance(item, Item):
                self.__char_inv.append(item.description)
        self.__armor_list = []
        for armor in self.armor:
            self.__armor_list.append(armor.description)

        return (self.name + " is wielding a " + self.weapon.description +
                " weapon and is wearing " + str(self.__armor_list) + ". They are carrying "
                + str(self.__char_inv) + ".\n Their stats are " + str(self.health)
                + " Health, " + str(self.__char_att) + " Attack, " + str(self.__char_def)
                + " Defense.")


class Player(Character):
    """The player character, gains consumable medical kits for healing.
     Inherits from the Character class.
    """
    def __init__(self, name: str) -> None:
        """Constructor for the Bard instance.
        Except:
            ValueError: The name passed in wasn't a string.
        """
        if isinstance(name, str):
            super().__init__(name)
        else:
            raise ValueError("The name passed in wasn't a string.")
        self.__med_kits = 5
        self.stats = 5

    @property
    def med_kits(self) -> int:
        """Getter for the __med_kits attribute.
        Returns:
            __med_kits (int) = Number of med kits on the character.
        """
        return self.__med_kits

    @med_kits.setter
    def med_kits(self, change: int):
        """Setter for the __med_kits attribute.
        Args:
            change (int): How much to change __med_kits by.
        """
        self.__med_kits += change
        if self.__med_kits < 0:
            self.__med_kits = 0

    def heal(self) -> int | None:
        """Heals yourself at the cost of a med kit.

        Returns:
            0: If you're out of med kits.
            amt (int): The amount you healed yourself for.
             Scales with your LV and intelligence.
        """
        if self.med_kits > 0:
            self.med_kits = -1
            amt = self.intelligence + self.level + 10
            tmp = self.health + amt
            if tmp >= self.max_health:
                amt = self.max_health - self.health
            self.health = amt
            print(self.name + " used a med kit and healed " + str(amt) + " health.")
            return amt
        else:
            print("No med kits left.")
            return 0

    def lv_up(self):
        tmp_lv = self.level
        tmp_xp = self.xp
        tmp_stats = self.stats
        while self.xp >= (self.level * 10):
            self.stats = 5
            self.xp = -(self.level * 10)
            self.level = 1
        print(f"Level: {tmp_lv} --> {self.level}")
        print(f"XP: {tmp_xp} --> {self.xp}")
        print(f"Stat Points: {tmp_stats} --> {self.stats}")
        while self.stats > 0:
            stat = input("What stat would you like to increase? Enter 'nothing' if you would like to stop.").lower()
            if stat == 'strength':
                self.strength = 1
                print(f"Strength: {self.strength - 1} --> {self.strength}\n")
            elif stat == 'dexterity':
                self.dexterity = 1
                print(f"Dexterity: {self.dexterity - 1} --> {self.dexterity}\n")
            elif stat == 'vitality':
                self.vitality = 1
                print(f"Vitality: {self.vitality - 1} --> {self.vitality}\n")
            elif stat == 'intelligence':
                self.intelligence = 1
                print(f"Intelligence: {self.intelligence - 1} --> {self.intelligence}\n")
            elif stat == "nothing":
                print("You decide to leave them alone for now.\n")
            else:
                print('Not a valid stat.\n')
            self.stats = -1


class Monster(Character):
    """The monster's to be fought, their stats depend on the default values
     specified in Character. Inherits from the Character class.
    """
    def __init__(self, name: str) -> None:
        """Constructor for the Monster instance.
        Except:
            ValueError: The name passed in wasn't a string.
        """
        if isinstance(name, str):
            super().__init__(name)
            self.__gold = randint(1, 10)
            if not Item.ITEMS:
                Item.load_items()
            if not Item.CONDITIONS:
                Item.load_conditions()
            if randint(1, 10) == 1:  # Turned in randint(1, 10) >= 1
                item = random.choice(Item.ITEMS)
                if "weapon" == item[0]:
                    self.add_inventory(Weapon(item))
                else:
                    self.add_inventory(Armor(item))
        else:
            raise ValueError("The name passed in wasn't a string.")

    def __str__(self) -> str:
        """String method that returns a monster's information.
        Returns:
            str: A string containing a monster's name, stats,
             the gold they have, and the item they're carrying.
        """

        self.__mon_inv = []
        if self.inventory():
            self.__mon_inv = self.inventory()[0]
            return ("LV " + str(self.level) + " " + self.name + " "
                    + str(self.health) + " Health, " + str(self.total_attack())
                    + " Attack and " + str(self.total_defense()) + " Defense.\n It is carrying " +
                    str(self.__gold) + " gold and an item of " +
                    str(self.__mon_inv.description) + ".")
        return ("LV " + str(self.level) + " " + self.name + " "
                + str(self.health) + " Health, " + str(self.total_attack())
                + " Attack and " + str(self.total_defense()) + " Defense"
                + " Luck.\n It is carrying " + str(self.__gold) + " gold.")

    @property
    def gold(self) -> int:
        """Getter for the __gold attribute.
        Returns:
            __gold (int): The gold coins a monster is carrying.
        """
        return self.__gold

    def lv_up(self):
        while self.xp >= (self.level * 10):
            self.stats = 5
            self.xp = -(self.level * 10)
            self.level = 1
        while self.stats > 0:
            stats = ['strength', 'dexterity', 'vitality', 'intelligence']
            stat = random.choice(stats)
            if stat == 'strength':
                self.strength = 1
            elif stat == 'dexterity':
                self.dexterity = 1
            elif stat == 'vitality':
                self.vitality = 1
            else:
                self.intelligence = 1
            self.stats = -1


class CharacterDeathException(Exception):
    """Exception for when a player character is killed.
    """
    def __init__(self, msg: str, character: object) -> None:
        """Constructor for the exception instance.
        Args:
            msg (str): The string message to be printed.
            character (object): Specifically, the player character that died.
        Except:
            ValueError: The msg passed in wasn't a string
            ValueError: The msg passed in cannot be an empty string.
            ValueError: The character passed in wasn't a Character object.
        """
        if not isinstance(msg, str):
            raise ValueError("The msg passed in must be a string.")
        if not msg:
            raise ValueError("The msg passed in cannot be an empty string.")
        if not isinstance(character, Character):
            raise ValueError("The character passed in must be a Character object.")
        super().__init__(msg)
        self.character = character


class MonsterDeathException(Exception):
    """Exception for when a monster is killed."""
    def __init__(self, msg: str, monster: Monster) -> None:
        """Constructor for the exception instance.
        Args:
            msg (str): The string message to be printed.
            monster (Monster): The monster that died.
        Except:
            ValueError: The msg passed in wasn't a string.
            ValueError: The msg must be a non-empty string.
            ValueError: The monster passed in wasn't a Monster object.
        """
        if not isinstance(msg, str):
            raise ValueError("The msg passed in must be a string.")
        if not msg:
            raise ValueError("The msg must be a non-empty string.")
        if not isinstance(monster, Monster):
            raise ValueError("The monster passed in must be a Monster object.")
        if not monster:
            raise ValueError("The monster passed in cannot be None.")
        super().__init__(msg)
        self.monster = monster


class CharacterOverweightException(Exception):
    """Exception for when a player character is carrying too much in their inventory.
    """
    def __init__(self, msg: str, character: Character) -> None:
        """Constructor for the exception instance.
        Args:
            msg (str): The string message to be printed.
            character (object): Specifically, the player character that is overburdened.
        Except:
            ValueError: The msg passed in wasn't a string
            ValueError: The msg must be a non-empty string.
            ValueError: The character passed in wasn't a Character object.
        """
        if not isinstance(msg, str):
            raise ValueError("The msg passed in must be a string.")
        if not msg:
            raise ValueError("The msg must be a non-empty string.")
        if not isinstance(character, Character):
            raise ValueError("The character passed in must be a Character object.")
        super().__init__(msg)
        self.character = character
