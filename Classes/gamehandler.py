"""Module for the GameHandler class.
"""
import math
import time
import tkinter
from Classes.GUI.FightGUI import FightGUI
from Classes.GUI.MainGui import MainGUI
from Classes.GUI.ChestGUI import ChestGUI
from Classes.GUI.ShopGUI import ShopGUI
from Classes.character import Player
from Classes.Map.map import Map


class GameHandler:
    """Manages the various game events.
    """
    def __init__(self):
        """Creates the instance.
        """
        self.player = Player("Default", {"Strength": 5, "Dexterity": 5, "Vitality": 5,
                                         "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5,
                                         "Credits": 0})
        self.map = Map()
        self.GUI = None
        self.FightGUI = None
        self.ShopGUI = None
        self.ChestGUI = None

        # Overall game stats
        self.initial_time = time.time()
        self.total_enemies_killed = 0
        self.total_rooms_entered = 0

        MainGUI(self.player, self)

    def start_new_game(self):
        """Starts a new game.
        """
        old_name = self.player.name
        self.player = Player(old_name, {"Strength": 5, "Dexterity": 5, "Vitality": 5,
                                        "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5,
                                        "Credits": 0})

        # Reset game stats
        self.initial_time = time.time()
        self.total_enemies_killed = 0
        self.total_rooms_entered = 0

        self.map = Map()
        self.GUI.create_main_gui()

    def get_map(self):
        """Getter for the map attribute.
        Returns:
            map (Map): The Map instance.
        """
        return self.map

    # For some reason python isn't happy if I set MainGUI above to a variable
    # so I have to do this
    def set_gui(self, gui):
        """Setter for the GUI attribute.
        Args:
            gui (MainGUI): The MainGUI instance.
        """
        self.GUI = gui
    
    def enter_room(self, room):
        """Method to enter a different room.
        Args:
            room (Room): The room in the map to enter.
        Returns:
            None: If a room event is still ongoing. i.e. Another window is still active.
        """
        self.map.set_current_room(room)
        self.GUI.display_buttons()

        if room.cleared:
            self.GUI.enter_repeated_room(room)
            return
        
        self.total_rooms_entered += 1

        match room.room_type:
            case "Combat":
                room.player = self.player
                room.lv_enemies()
                self.GUI.enter_combat_room(room)
                self.FightGUI = FightGUI(room, self.player, self)
            case "Chest":
                self.GUI.enter_chest_room(room)
                self.ChestGUI = ChestGUI(room, self.player, self)
            case "Shop":
                self.GUI.enter_shop_room(room)
                self.ShopGUI = ShopGUI(room, self.player, self)
            case "Boss":
                self.GUI.enter_boss_room(room)
                self.FightGUI = FightGUI(room, self.player, self)
            case "Start":
                room.clear_room(True)

    def exit_room(self, room):
        """Method to exit a room.
        Args:
            room (Room): Room instance to exit.
        """
        room.clear_room(True)

        if room.room_type == "Boss":
            self.GUI.exit_boss_room()
            self.total_enemies_killed += 1
        elif room.room_type == "Combat":
            self.total_enemies_killed += room.enemies_killed
            self.GUI.exit_combat_room(room)
        else:
            self.GUI.exit_room(room)

    def end_game(self, is_game_won: bool):
        """Ends the game and display corresponding GUI.
        Args:
            is_game_won (bool): If the game has been won or lost.
        """
        
        # Display to player total time spent 
        total_time = math.trunc(time.time() - self.initial_time)

        if is_game_won:
            self.GUI.display_game_won_gui(total_time, self.total_enemies_killed,
                                          self.total_rooms_entered)
        else:
            self.GUI.display_game_lost_gui(total_time, self.total_enemies_killed,
                                           self.total_rooms_entered)
