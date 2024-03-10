"""Module for the CharacterGUI class.
"""

import tkinter as tk
from PIL import ImageTk, Image
from Classes.character import Player
from Classes.Rooms.room import Room

class CharacterGUI(tk.Toplevel):
    """Class governing all player-game interactions involving the Character's stats.
    """
    def __init__(self, player: Player, room: Room, gui):
        """Creates the instance.
        Args:
            player (Player): The Player instance to interact with.
            room (Room): The current room the Player is in.
            gui: The parent gui.
        """
        super().__init__()
        self.title("Character Screen")
        self.geometry(f'{300}x{500}+400+50')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.minsize(self.width, self.height)  # Minimum size of the window, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.player = player
        self.room = room
        self.gui = gui

        # Customize screen
        self.original_image = Image.open('Images/Stats.jpg').resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height, bg="#043F5B")
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        exit_button = tk.Button(self, text="Close", font="Time_New_Roman 15",
                                     command=self.destroy)
        self.bg_canvas.create_window(self.width / 2 + 80, 475,anchor='sw',window=exit_button)

        self.update_character_gui()

        self.mainloop()

    def stat_button(self, stat: str, amount: int):
        """Method governing what happens when a stat-increase button is pressed.
        Args:
            stat (str): The stat to be affected.
            amount (int): How much to increase the stat by.
        """
        if self.player.stats["Stat Points"] > 0:
            self.player.upgrade_stats(stat, amount)
            if stat == "Vitality":
                self.player.update_max_health()
                self.player.stats["Health"] += 5
                self.player.update_max_health()
                self.player.update_defense()
            if stat == "Strength":
                self.player.update_attack()
        self.update_character_gui()

    def level_up(self):
        """Method to increase the player's level when the button is clicked.
        """
        self.player.lv_up()
        if self.player.stats["XP"] < self.player.stats["Level"] * 10:
            self.bg_canvas.delete("level_up")
        self.update_character_gui()

    def update_character_gui(self):
        """Method to update the display whenever a button is clicked.
        """
        self.bg_canvas.delete("stats")
        self.bg_canvas.delete("str_up", "dex_up", "vit_up", "int_up")
        self.bg_canvas.delete("level_up")
        self.bg_canvas.create_text(self.width / 2 - 30, self.height - 225,
                                   font="Time_New_Roman 15", fill="#038787", justify="center",
                                   text=self.player.name + "'s Stats" +
                                   "\n\nHealth: " + str(self.player.stats["Health"]) +
                                   "/" + str(self.player.stats["Max Health"]) +
                                   "\n\nStr: " + str(self.player.stats["Strength"]) +
                                   "\n\nDex: " + str(self.player.stats["Dexterity"]) +
                                   "\n\nVit: " + str(self.player.stats["Vitality"]) +
                                   "\n\nInt: " + str(self.player.stats["Intelligence"]) +
                                   "\n\nFree Points: " + str(self.player.stats["Stat Points"]) +
                                   "\n\nLevel: " + str(self.player.stats["Level"]) +
                                   "\n\nXP: " + str(self.player.stats["XP"]) +
                                   "/" + str(self.player.stats["Level"] * 10), tags="stats")
        if self.player.stats["Stat Points"] > 0:
            str_up = tk.Button(self, font=5, width=1, height=1, text="+",
                               command=lambda: self.stat_button("Strength", 1))
            self.bg_canvas.create_window(self.width / 2 + 30, self.height - 315, anchor='center',
                                         window=str_up, tags="str_up")

            dex_up = tk.Button(self, font=5, width=1, height=1, text="+",
                               command=lambda: self.stat_button("Dexterity", 1))
            self.bg_canvas.create_window(self.width / 2 + 30, self.height - 265, anchor='center',
                                         window=dex_up, tags="dex_up")

            vit_up = tk.Button(self, font=5, width=1, height=1, text="+",
                               command=lambda: self.stat_button("Vitality", 1))
            self.bg_canvas.create_window(self.width / 2 + 30, self.height - 215, anchor='center',
                                         window=vit_up, tags="vit_up")

            int_up = tk.Button(self, font=5, width=1, height=1, text="+",
                               command=lambda: self.stat_button("Intelligence", 1))
            self.bg_canvas.create_window(self.width / 2 + 30, self.height - 165, anchor='center',
                                         window=int_up, tags="int_up")
        if self.player.stats["XP"] >= self.player.stats["Level"] * 10:
            level_up = tk.Button(self, font=3, width=5, height=1, text="LV-Up",
                               command=lambda: self.level_up())
            self.bg_canvas.create_window(self.width / 2 + 60, self.height - 85, anchor='center',
                                         window=level_up, tags="level_up")

    def destroy(self):
        """Method governing what happens when the window is destroyed.
        """
        self.room.clear_room(True)
        self.gui.ready = True
        super().destroy()
