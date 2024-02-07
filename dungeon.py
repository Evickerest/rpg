"""Creates the dungeon room.

Phuc Le
11/9/2023
Version 3.0
"""

import random
from character import *
from item import *


class Dungeon:
    """Contains information about the dungeon room itself and how the rooms
     are connected to one another.
    """
    ROOM_DETAILS = []

    @staticmethod
    def load_room_details() -> None:
        """Static method to load the different room details from a file.
        """
        with open('room_names', 'r') as f:
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
        self.__monsters: list[Monster] = []
        self.__prior = None
        self.__next = None
        self.__num_monsters = 0
        self.__shop = False
        self.__combat = False
        self.__loot = False
        self.__healing = False
        self.set_room_type()

        self.__monster_list = []
        with open("monster_names") as f:
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
        if self.combat:
            self.__num_monsters = randint(0, 4)
            for num in range(0, self.__num_monsters):
                monster_name = random.choice(self.__monster_list)
                mon = Monster(monster_name)
                if not (self.monster_in_dungeon(mon) in self.__monsters):
                    self.__monsters.append(mon)
        else:
            raise ValueError("This isn't a combat room.")

    def monster_in_dungeon(self, mon: Monster) -> Monster | None:
        """Checks if the monster with the specified name is already in the dungeon.
        Args:
            mon (Monster): The Monster instance to check for.
        Except:
            ValueError: If the mon_name isn't a Monster type.
        """
        if not isinstance(mon, Monster):
            raise ValueError("mon must be a Monster object.")

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

    @prior.setter
    def prior(self, _prior: object) -> None:
        """Setter for the __prior attribute.
        Args:
            _prior (object): The Dungeon object that is designed to come before the current one.
        Except:
            ValueError: The prior dungeon is not a Dungeon object.
        """
        if isinstance(_prior, Dungeon):
            self.__prior = _prior
        else:
            raise ValueError("The prior dungeon is not a Dungeon object.")

    @property
    def next(self) -> type[object]:
        """Getter for the __next attribute.
        Returns:
            __next (type[object]): Specifically, the Dungeon instance next to
             this one.
        """
        return self.__next

    @next.setter
    def next(self, _next) -> None:
        """Setter for the __next attribute.
        Args:
            _next (object): The Dungeon object that is designed to come after the current one.
        Except:
            ValueError: The _next dungeon is not a Dungeon object.
        """
        if isinstance(_next, Dungeon):
            self.__next = _next
        else:
            raise ValueError("The _next dungeon is not a Dungeon object.")

    @property
    def shop(self) -> bool:
        """Getter for the __shop attribute.
        Returns:
            __shop (bool): Whether this room is a shop.
        """
        return self.__shop

    @shop.setter
    def shop(self, _bool: bool) -> None:
        """Setter for the __bool attribute.
        Args:
            _bool (bool): The boolean that determines if this room is a shop.
        Except:
            ValueError: The _bool value is not a boolean.
        """
        if isinstance(_bool, bool):
            self.__shop = _bool
        else:
            raise ValueError("The _bool value is not a boolean.")

    @property
    def combat(self) -> bool:
        """Getter for the __combat attribute.
        Returns:
            __combat (bool): Whether this room is a combat room.
        """
        return self.__combat

    @combat.setter
    def combat(self, _bool: bool) -> None:
        """Setter for the __combat attribute.
        Args:
            _bool (bool): The boolean that determines if this room is a combat room.
        Except:
            ValueError: The _bool value is not a boolean.
        """
        if isinstance(_bool, bool):
            self.__combat = _bool
        else:
            raise ValueError("The _bool value is not a boolean.")

    @property
    def loot(self) -> bool:
        """Getter for the __loot attribute.
        Returns:
            __loot (bool): Whether this room is a loot room.
        """
        return self.__loot

    @loot.setter
    def loot(self, _bool: bool) -> None:
        """Setter for the __loot attribute.
        Args:
            _bool (bool): The boolean that determines if this room is a loot room.
        Except:
            ValueError: The _bool value is not a boolean.
        """
        if isinstance(_bool, bool):
            self.__loot = _bool
        else:
            raise ValueError("The _bool value is not a boolean.")

    @property
    def healing(self) -> bool:
        """Getter for the __healing attribute.
        Returns:
            __loot (bool): Whether this room is a healing room.
        """
        return self.__healing

    @healing.setter
    def healing(self, _bool: bool) -> None:
        """Setter for the __healing attribute.
        Args:
            _bool (bool): The boolean that determines if this room is a healing room.
        Except:
            ValueError: The _bool value is not a boolean.
        """
        if isinstance(_bool, bool):
            self.__healing = _bool
        else:
            raise ValueError("The _bool value is not a boolean.")

    def stock_store(self):
        if not Item.ITEMS:
            Item.load_items()
        if not Item.CONDITIONS:
            Item.load_conditions()
        if self.shop:
            num = random.randint(2, 5)
            for i in range(0, num):
                item = random.choice(Item.ITEMS)
                if "weapon" == item[0]:
                    self.items.append(Weapon(item))
                else:
                    self.items.append(Armor(item))
        else:
            raise ValueError("This isn't a shop")

    def stock_loot(self):
        if not Item.ITEMS:
            Item.load_items()
        if not Item.CONDITIONS:
            Item.load_conditions()
        if self.loot:
            item = random.choice(Item.ITEMS)
            if "weapon" == item[0]:
                self.items.append(Weapon(item))
            else:
                self.items.append(Armor(item))
        else:
            raise ValueError("This isn't a shop")

    def buy_item(self, store_item: Item, player: Player):
        if not isinstance(player, Player):
            print("Not a player, you can't buy items!")
        else:
            self.items.remove(store_item)
            player.add_inventory(store_item)
            if player.credits >= store_item.value:
                player.credits = -store_item.value

    def sell_item(self, inventory_item: Item, player: Player):
        if not isinstance(player, Player):
            print("Not a player, you can't sell items!")
        else:
            self.items.remove(inventory_item)
            player.credits = inventory_item.sell_value

    def set_room_type(self):
        num = random.randint(0, 5)
        if num == 1:
            self.shop = True
        if num == 2:
            self.combat = True
        if num == 3:
            self.loot = True
        if num == 4:
            self.healing = True
