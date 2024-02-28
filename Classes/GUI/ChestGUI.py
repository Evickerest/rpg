import tkinter as tk
from Classes.Character import *
from Classes.Rooms.ChestRoom import ChestRoom
from PIL import ImageTk, Image


class ChestGUI(tk.Toplevel):
    def __init__(self, room: ChestRoom, player: Player):
        super().__init__()
        self.title("Chest Screen")
        self.geometry(f'{300}x{400}+400+50')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.minsize(self.width, self.height)  # Minimum size of the window, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.player = player
        self.room = room

        self.original_image = Image.open('Images/bg2.jpeg').resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height, bg="#043F5B")
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        if self.room.item:
            self.loot_button = tk.Button(self, text=f"Take " + str(self.room.item.stats["name"]),
                                         font='Time_New_Roman 8', command=lambda: self.loot_chest())
            self.loot_button_window = self.bg_canvas.create_window(100, 200, anchor='sw',
                                                                   window=self.loot_button,
                                                                   tags="loot_button")

            self.scrap_button = tk.Button(self, text=f"Scrap It",
                                          font='Time_New_Roman 8', command=lambda: self.scrap_chest())
            self.scrap_button_window = self.bg_canvas.create_window(100, 300, anchor='sw',
                                                                    window=self.scrap_button,
                                                                    tags="scrap_button")

    def loot_chest(self):
        self.player.inventory.append(self.room.item)
        self.room.item = None
        self.bg_canvas.delete("loot_button", "scrap_button")
        self.destroy()

    def scrap_chest(self):
        self.player.stats["Credits"] += self.room.item.stats["value"]
        self.room.item = None
        self.bg_canvas.delete("loot_button", "scrap_button")
        self.destroy()

    def destroy(self):
        self.room.clearRoom(True)
        super().destroy()
