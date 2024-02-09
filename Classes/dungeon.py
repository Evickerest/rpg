"""Creates the dungeon room.

Phuc Le
11/9/2023
Version 3.0
"""
import csv
import random
from random import *
from Classes.Character import *
from Classes.Item import *
import csv

class Dungeon:
    """Contains information about the dungeon room itself and how the rooms
     are connected to one another.
    """
    ROOM_DETAILS = []

    @staticmethod
    def load_room_details() -> None:
        """Static method to load the different room details from a file.
        """
        with open('Classes/room_txt/room_names', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                Dungeon.ROOM_DETAILS.append(row)

    def __init__(self, name: str, description: str) -> None:
        """Constructor Method for the Dungeon instance.
        Args:
            name (str): The room's name.
            description (str): The room's description
        Except:
            ValueError: The dungeon's name must be a non-empty string.
            ValueError: The dungeon's description must be a non-empty string.
        """
        if isinstance(name, str) and name != "":
            self.__name = name
        else:
            raise ValueError("The dungeon's name must be a non-empty string.")

        if isinstance(description, str) and description != "":
            self.__description = description
        else:
            raise ValueError("The dungeon's description must be a non-empty string.")

        self.__items: list[Item] = []
        self.__monsters: list[Enemy] = []
        self.__prior = None
        self.__next = None
        self.__num_monsters = 0

        self.__monster_list = []
        with open("Classes/enemy_txt/monster_names") as f:
            self.__monster_list = f.readlines()

        if not Dungeon.ROOM_DETAILS:
            Dungeon.load_room_details()
        if not self.__name:
            details = random.choice(Dungeon.ROOM_DETAILS)
            self.__name = details[0]
            self.__description = details[1]

    def generate(self) -> None:
        """Generates the Dungeon and fills it with a random number
         of enemies from 0-4 inclusive.
        """
        self.__num_monsters = randint(0, 4)
        for num in range(0, self.__num_monsters):
            monster_name = random.choice(self.__monster_list)
            mon = Enemy(monster_name)
            if not (self.monster_in_dungeon(mon) in self.__monsters):
                self.__monsters.append(mon)

    def monster_in_dungeon(self, mon: Enemy) -> Enemy | None:
        """Checks if the enemy with the specified name is already in the dungeon.
        Args:
            mon (Enemy): The Enemy instance to check for.
        Except:
            ValueError: If the mon_name isn't an Enemy type.
        """
        if not isinstance(mon, Enemy):
            raise ValueError("mon must be a Enemy object.")

        for monster in self.monsters:
            if mon == monster:
                return monster
        return None

    def __str__(self) -> str:
        """String Method that gives the dungeon name, its description, and any items it has.
        Returns:
            __room_str (str): The string containing the dungeon's name, its description,
             and the list of items it has.
        """
        self.__room_inv = []
        for item in self.__items:
            self.__room_inv.append(item.description)
        self.__room_str = (str(self.__name) + ". " + str(self.__description) +
                           ". Items: " + str(self.__room_inv))
        return self.__room_str

    def __show_monsters__(self) -> str:
        """Returns a string if monsters are present in the room.
        Returns:
            str: If no monsters are present, 'No monsters (whew!)'.
            monster_str (str): Otherwise, a string containing the name
             of all monsters present in the room.
        """
        monster_str = "Monsters in Room:\n "
        for monster in self.__monsters:
            monster_str = monster_str + str(monster.name) + " "
        if not self.__monsters:
            return "No monsters (whew!)."
        return monster_str

    @property
    def name(self) -> str:
        """Getter for the __name attribute.
        Returns:
            __name (str): The name of this room.
        """
        return self.__name

    @property
    def description(self) -> list:
        """Getter for the __description attribute.
        Returns:
            __description (str): The description of this room.
        """
        return self.__description

    @property
    def monsters(self) -> list:
        """Getter for the __monsters attribute.
        Returns:
            __monsters (list): The list of Monster instances in the dungeon.
        """
        return self.__monsters

    @property
    def items(self) -> list:
        """Getter for the __items attribute.
        Returns:
            __items (list): The list of Item instances in the dungeon.
        """
        return self.__items

    @property
    def prior(self) -> type[object]:
        """Getter for the __prior attribute.
        Returns:
            __prior (type[object]): Specifically, the Dungeon instance prior to
             this one. The first room will have no prior Dungeon instance.
        """
        return self.__prior
