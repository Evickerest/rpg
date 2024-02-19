import tkinter as tk
from Classes.Character import *
from PIL import ImageTk, Image

class CharacterGUI(tk.Tk):
    def __init__(self, player: Player):
        super().__init__()
        self.title("Character Screen")
        self.geometry(f'{250}x{400}+170+250')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.minsize(self.width, self.height)  # Minimum size of the window, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.player = player

        # Customize screen
        self.original_image = Image.open('Images/bg2.jpeg').resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height, bg="black")
        self.bg_canvas.pack(fill='both', expand=True)

        self.exit_button = tk.Button(self, text="Close", font="Time_New_Roman 10", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width / 2 - 60, 380,
                                                               anchor='sw', window=self.exit_button)

        self.updateCharacterGui()

        if self.player.stats["Stat Points"] > 0:
            str_up = tk.Button(self, font=5, width=1, height=1, text="+",
                               command=lambda: self.stat_button("Strength", 1))
            self.bg_canvas.create_window(self.width / 2 + 30, self.height - 265, anchor='center',
                                         window=str_up, tags="str_up")

            dex_up = tk.Button(self, font=5, width=1, height=1, text="+",
                               command=lambda: self.stat_button("Dexterity", 1))
            self.bg_canvas.create_window(self.width / 2 + 30, self.height - 215, anchor='center',
                                         window=dex_up, tags="dex_up")

            vit_up = tk.Button(self, font=5, width=1, height=1, text="+",
                               command=lambda: self.stat_button("Vitality", 1))
            self.bg_canvas.create_window(self.width / 2 + 30, self.height - 165, anchor='center',
                                         window=vit_up, tags="vit_up")

            int_up = tk.Button(self, font=5, width=1, height=1, text="+",
                               command=lambda: self.stat_button("Intelligence", 1))
            self.bg_canvas.create_window(self.width / 2 + 30, self.height - 115, anchor='center',
                                         window=int_up, tags="int_up")

        self.mainloop()

    def stat_button(self, stat: str, amount: int):
        if self.player.stats["Stat Points"] > 0:
            self.player.upgradeStats(stat, amount)
        if stat == "Vitality":
            self.player.updateMaxHealth()
            self.player.stats["Health"] = self.player.stats["Max Health"]
        self.updateCharacterGui()

    def updateCharacterGui(self):
        self.bg_canvas.delete("stats")
        self.bg_canvas.create_text(self.width / 2 - 30, self.height - 220, font=10, fill="blue", justify="center",
                                   text=self.player.name + "'s Stats" +
                                        "\n\nHealth: " + str(self.player.stats["Health"]) +
                                        "/" + str(self.player.stats["Max Health"]) +
                                        "\n\nStr: " + str(self.player.stats["Strength"]) +
                                        "\n\nDex: " + str(self.player.stats["Dexterity"]) +
                                        "\n\nVit: " + str(self.player.stats["Vitality"]) +
                                        "\n\nInt: " + str(self.player.stats["Intelligence"]) +
                                        "\n\nFree Points: " + str(self.player.stats["Stat Points"]), tags="stats")
        if self.player.stats["Stat Points"] == 0:
            self.bg_canvas.delete("str_up", "dex_up", "vit_up", "int_up")


