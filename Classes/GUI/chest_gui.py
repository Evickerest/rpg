"""Module containing the ChestGUI class.
"""

import tkinter as tk
from PIL import ImageTk, Image
from Classes.GUI.button import Button
from Classes.character import Player
from Classes.Rooms.chest_room import ChestRoom


class ChestGUI(tk.Toplevel):
    """Class containing potential actions when a ChestRoom is entered
     in the game.
    """
    def __init__(self, room: ChestRoom, player: Player, gameHandler):
        """Creates the instance.
        Args:
            room (ChestRoom): The ChestRoom instance.
            player (Player): The Player instance.
            gameHandler: The game_handler instance.
        """
        super().__init__()
        self.title("Chest Screen")
        self.geometry(f'{300}x{400}+400+50')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.minsize(self.width, self.height)  # Min size, can be maximized.
        self.iconbitmap('Images/LevelOne/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.player = player
        self.room = room

        self.game_handler = gameHandler

        self.original_image = Image.open('Images/LevelOne/bg2.jpeg').resize((self.width,
                                                                    self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height,
                                   bg="#043F5B")
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        if self.room.item:
            Button(self, f"Take {self.room.item.stats['name']}", self.loot_chest, 100, 200, font=("Times New Roman", 8), tags="loot_button")
            Button(self, f"Scrap It For {self.room.item.stats['value']} Credits", self.scrap_chest, 100, 300,  font=("Cambria Math",9,"bold"), tags="scrap_button")

    def loot_chest(self):
        """Method for what happens if the player chooses to take the item.
        """
        self.player.inventory.append(self.room.item)
        self.room.item = None
        self.bg_canvas.delete("loot_button", "scrap_button")
        self.destroy()

    def scrap_chest(self):
        """Method for what happens if the player chooses to scrap the item
         and gain Credits instead.
        """
        self.player.stats["Credits"] += self.room.item.stats["value"]
        self.room.item = None
        self.bg_canvas.delete("loot_button", "scrap_button")
        self.destroy()

    def destroy(self):
        """Method governing what happens when the instance is destroyed.
        """
        self.room.clear_room(True)
        self.game_handler.exit_room(self.room)
        super().destroy()
