"""Stores information about the various weapons and armors that characters
 can wear/equip in the non-abstract Weapon and Armor classes.

Phuc Le
11/9/2023
Version 3.0
"""


import abc
import csv
import random
from typing import List


class Item(abc.ABC):
    """ABC that contains information about an abstract item.
    Attributes:
        CONDITIONS (List[List[str]]): The list containing all the potential
         conditions an item can have.
        ITEMS (List[List[str]]): The list containing all the potential item types.
    """
    CONDITIONS: List[List[str]] = []
    ITEMS: List[List[str]] = []

    @staticmethod
    def load_conditions() -> None:
        """Static method to load the different conditions an item can be in from a specified file.
        """
        with open('item_attributes', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                Item.CONDITIONS.append(row)

    @staticmethod
    def load_items() -> None:
        """Static method to load the different types of items from a specified file.
        """
        with open('item_types', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                Item.ITEMS.append(row)

    def __init__(self, attributes: list) -> None:
        """The constructor for the Item instance.
            Args:
                attributes (list): The list of attributes an item has.
            Except:
                ValueError: If the attributes passed to the instance wasn't a list.
                ValueError: If the attributes list was of length 4 or less.
                ValueError: If the first element in the list wasn't a string.
                ValueError: If the second element in the list wasn't a string.
                ValueError: If the attributes[4] value wasn't a string or an integer.
                ValueError: If the attributes[4] value can't be turned into an integer through int().
            """
        if not isinstance(attributes, list):
            raise ValueError("The attributes passed to the Item instance must be"
                             " in a list.")
        if not len(attributes) >= 5:
            raise ValueError("The attributes list must have at least 5 entries.")
        if not isinstance(attributes[0], str):
            raise ValueError("The first element in the list must be a string.")
        if not isinstance(attributes[1], str):
            raise ValueError("The second element in the list must be a string.")
        if not isinstance(attributes[4], str) and not isinstance(attributes[4], int):
            raise ValueError("The fourth entry in the attribute list must be a string or an integer.")
        try:
            self.__weight = int(attributes[4])
        except ValueError:
            raise ValueError("The fourth entry in the attribute list can't be turned into an integer through int().")
        self.__attributes = attributes
        self.__name = attributes[1]

        if not Item.CONDITIONS:
            Item.load_conditions()
        condition = random.choice(Item.CONDITIONS)
        self.condition = condition

    @property
    def name(self) -> str:
        """Getter for the __name attribute.
        Returns:
            __name (str): The item's name.
        """
        return self.__name

    @property
    def description(self) -> str:
        """Method that returns a short description of an item.
        Returns:
            str: A short string of an item's condition and name.
        """
        return self.__condition[0] + " " + self.__name

    @property
    def condition(self) -> list:
        """Getter for the __condition attribute.
        Returns:
            __condition (list): A list about the condition of an item.
        """
        return self.__condition

    @condition.setter
    def condition(self, _condition: list) -> None:
        """Setter for the __condition attribute.
        Args:
            _condition (list): An item's condition as a list with types [str, float].
        Except:
            ValueError: The item's conditions must be in the form of a list.
            ValueError: The item's list of conditions must have at least 2 entries.
            ValueError: The first element in the list of conditions must be a string.
            ValueError: The second element in the list of conditions must be a string or a float.
        """
        if not isinstance(_condition, list):
            raise ValueError("The item's conditions must be in the form of a list.")
        if len(_condition) < 2:
            raise ValueError("The item's list of conditions must have at least 2 entries.")
        if not isinstance(_condition[0], str):
            raise ValueError("The first index value must be a string.")
        if not isinstance(_condition[1], str) and not isinstance(_condition[1], float):
            raise ValueError("The second index value must be a string or a float.")
        self.__condition = _condition

    @property
    def weight(self) -> int:
        """Getter for the __weight attribute.
        Returns:
            __weight (int): The weight of an item as an integer.
        """
        return self.__weight

    @property
    def attributes(self) -> list:
        """Getter for the __attributes attribute.
        Returns:
            __attributes (list): The list of attributes an item's contain.
        """
        return self.__attributes


class Armor(Item):
    """Stores information about an armor piece. Inherits from the Item class.
    """
    def __init__(self, attributes) -> None:
        """The constructor for the Armor instance.
        Args:
            attributes (list): The list of attributes an armor piece has.
        Except:
            ValueError: If the attributes passed to this instance wasn't a list.
            ValueError: If the list passed in had less than 5 elements.
            ValueError: If the first entry in the list wasn't 'armor'.
        """
        if not isinstance(attributes, list):
            raise ValueError("The attributes passed in wasn't a list.")
        if len(attributes) < 5:
            raise ValueError("The attributes list passed in must have at least 5 entries.")
        if attributes[0] != "armor":
            raise ValueError("The 1st entry in the list wasn't 'armor'.")
        super().__init__(attributes)
        self.added_defense = self.attributes
        self.__armor_type = attributes[1]

    @property
    def added_defense(self) -> int:
        """Getter for the added_defense attribute.
        Returns:
            __added_defense (int): The defense increase provided by an armor piece.
        """
        return self.__added_defense

    @added_defense.setter
    def added_defense(self, attributes: list) -> None:
        """Setter for the defense an armor piece adds.
        Args:
            attributes (list): The list of attributes this armor piece has.
        Except:
            ValueError: If the armor's attributes aren't given as a list.
            ValueError: If the fourth entry in the attribute list wasn't an integer or a string.
            ValueError: If the second entry in the armor's condition wasn't a string or a float.
            ValueError: If the attribute list had less than 5 entries.
        """
        if not isinstance(attributes, list):
            raise ValueError("The attributes passed in must be in a list.")
        if not len(attributes) >= 5:
            raise ValueError("The list must have at least 5 entries.")
        if not isinstance(attributes[3], int) and not isinstance(attributes[3], str):
            raise ValueError("The fourth element in the attribute list must be an integer or a string.")
        if not isinstance(self.condition[1], str) and not isinstance(self.condition[1], float):
            raise ValueError("The second element in the condition list must be a string or a float.")
        self.__added_defense = round(float(attributes[3]) * float(self.condition[1]))

    @property
    def type(self) -> str:
        """Getter for the type attribute.
        Returns:
            __armor_type (str): The type of armor.
        """
        return self.__armor_type


class Weapon(Item):
    """Stores information about a weapon. Inherits from the Item class.
    """
    def __init__(self, attributes: list) -> None:
        """The constructor for the Weapon class.
        Args:
            attributes (list): The list of attributes a weapon has.
        Except:
            ValueError: If the attributes passed to this instance wasn't a list.
            ValueError: If the list passed in was less than 5 elements.
            ValueError: If the first entry in the list wasn't 'weapon'.
        """
        if not isinstance(attributes, list):
            raise ValueError("The attributes passed in wasn't a list.")
        if len(attributes) < 5:
            raise ValueError("The attributes list passed in must have at least 5 entries.")
        if attributes[0] != "weapon":
            raise ValueError("The 1st entry in the list wasn't 'weapon'.")
        super().__init__(attributes)
        self.added_attack = self.attributes

    @property
    def added_attack(self) -> int:
        """Getter for the added_attack attribute.
        Returns:
            __added_attack (int): The attack increase provided by a weapon.
        """
        return self.__added_attack

    @added_attack.setter
    def added_attack(self, attributes: list) -> None:
        """Setter for the attack a weapon adds.
        Args:
            attributes (list): The list of attributes this weapon has.
        Except:
            ValueError: If the weapon's attributes aren't given as a list.
            ValueError: If the third entry in the attribute list wasn't an integer or a string.
            ValueError: If the second entry in the weapon's condition wasn't a string or a float.
            ValueError: If the attribute list had less than 5 entries.
        """
        if not isinstance(attributes, list):
            raise ValueError("The attributes passed in must be in a list.")
        if not len(attributes) >= 5:
            raise ValueError("The list must have at least 5 entries.")
        if not isinstance(attributes[2], int) and not isinstance(attributes[2], str):
            raise ValueError("The third element in the attribute list must be an integer or a string.")
        if not isinstance(self.condition[1], str) and not isinstance(self.condition[1], float):
            raise ValueError("The second element in the condition list must be a string or a float.")
        self.__added_attack = round(float(attributes[2]) * float(self.condition[1]))
