"""Module for the GameHandler class.
"""
import math
import tkinter
from Classes.GUI.FightGUI import FightGUI
from Classes.GUI.MainGui import MainGUI
from Classes.GUI.ChestGUI import ChestGUI
from Classes.GUI.ShopGUI import ShopGUI
from Classes.character import Player
from Classes.Map.map import Map
import time


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

        # Overall game stats
        self.initialTime = time.time()
        self.totalEnemiesKilled = 0
        self.totalRoomsEntered = 0

        MainGUI(self.player, self)

    def startNewGame(self):
        """Starts a new game.
        """
        oldName = self.player.name
        self.player = Player(oldName, {"Strength": 5, "Dexterity": 5, "Vitality": 5,
                                         "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5,
                                         "Credits": 0})
        # Reset game stats
        self.initialTime = time.time()
        self.totalEnemiesKilled = 0
        self.totalRoomsEntered = 0

        self.map = Map()
        self.GUI.createMainGUI()

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
            None: If a room event is still ongoing. i.e Another window is still active.
        """
        self.map.set_current_room(room)
        self.GUI.display_buttons()

        if room.cleared:
            self.GUI.enterRepeatedRoom(room)
            return
        
        self.totalRoomsEntered += 1

        match room.room_type:
            case "Combat":
                room.player = self.player
                room.lv_enemies()
                self.GUI.enterCombatRoom(room)
                self.FightGUI = FightGUI(room, self.player, self)
            case "Chest":
                self.GUI.enterChestRoom(room)
                self.ChestGUI = ChestGUI(room, self.player, self)
            case "Shop":
                self.GUI.enterShopRoom(room)
                self.ShopGUI = ShopGUI(room, self.player, self)
            case "Boss":
                self.GUI.enterBossRoom(room)
                self.FightGUI = FightGUI(room, self.player, self)
            case "Start":
                room.clear_room(True)

    def exit_room(self, room):
        """Method to exit a room.
        """
        room.clear_room(True)

        if room.room_type == "Boss":
            self.GUI.exitBossRoom()
            self.totalEnemiesKilled += 1
        elif room.room_type == "Combat":
            self.totalEnemiesKilled += room.enemiesKilled
            self.GUI.exitCombatRoom(room)
        else:
            self.GUI.exit_room(room)

    def end_game(self, isGameWon: bool):
        """Ends the game and display corresponding GUI.
        Args:
            isGameWon (bool): If the game has been won or lost.
        """
        
        # Display to player total time spent 
        totalTime = math.trunc(time.time() - self.initialTime)

        if isGameWon:
            self.GUI.displayGameWonGUI(totalTime, self.totalEnemiesKilled, self.totalRoomsEntered)
        else:
             self.GUI.displayGameLostGUI(totalTime, self.totalEnemiesKilled, self.totalRoomsEntered)
