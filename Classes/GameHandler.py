import tkinter

from Classes.GUI.FightGUI import FightGUI
from Classes.GUI.MainGui import MainGUI
from Classes.GUI.ChestGUI import ChestGUI
from Classes.GUI.ShopGUI import ShopGUI
from Classes.Character import Player
from Classes.Map.Map import Map

class GameHandler:
    def __init__(self):
        self.player = Player("Default", {"Strength": 5, "Dexterity": 5, "Vitality": 5,
                             "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5, "Credits": 0}) 
        self.map = Map()
        self.GUI = None
        MainGUI(self.player, self)


    def getMap(self):
        return self.map

    # For some reason python isn't happy if I set MainGUI above to a variable so I have to do this
    def setGUI(self, GUI):
        self.GUI = GUI
    
    def enterRoom(self, room):
        self.map.setCurrentRoom( room )
        self.GUI.display_buttons()

        if room.cleared:
            self.GUI.enterRepeatedRoom(room)
            return

        match room.roomType:
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
                room.clearRoom(True)

    def exitRoom(self, room):
        room.clearRoom(True)

        if room.roomType == "Boss":
            self.GUI.exitBossRoom(room)
        elif room.roomType == "Combat":
            self.GUI.exitCombatRoom(room)
        else:
            self.GUI.exitRoom(room)
        



      


