import tkinter as tk
from Classes.Character import *
from Classes.Rooms.CombatRoom import CombatRoom
from Classes.Rooms.Room import *
from PIL import ImageTk, Image


class FightGUI(tk.Tk):
    def __init__(self, room: CombatRoom, player: Player):
        super().__init__()
        self.title("Combat Screen")
        self.geometry(f'{800}x{600}+170+250')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.minsize(self.width, self.height)  # Minimum size of the window, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.player = player
        self.enemy = room.monsters

        self.no_enemy = False

        self.original_image = Image.open('Images/bg2.jpeg').resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height, bg="black")
        self.bg_canvas.pack(fill='both', expand=True)

        self.bg_canvas.create_text(self.width / 2 - 250, self.height - 580, font=10, fill="blue", justify="center",
                                   text=self.player.name + "'s Side", tags="equipment_title")
        self.bg_canvas.create_text(self.width / 2 + 250, self.height - 580, font=10, fill="blue", justify="center",
                                   text=self.enemy.name + "'s Side", tags="inventory_title")

        self.attack_button = tk.Button(self, text='Attack',
                                       font='Time_New_Roman 8', command=lambda: self.use_medkit())
        self.attack_button_window = self.bg_canvas.create_window(50, 400, anchor='sw',
                                                                 window=self.attack_button, tags="attack_button")

        self.defend_button = tk.Button(self, text='Defend',
                                       font='Time_New_Roman 8', command=lambda: self.use_medkit())
        self.defend_button_window = self.bg_canvas.create_window(250, 400, anchor='sw',
                                                                 window=self.defend_button, tags="defend_button")

        self.use_medkit_button = tk.Button(self, text='Use Medkit',
                                           font='Time_New_Roman 8', command=lambda: self.use_medkit())
        self.use_medkit_button_window = self.bg_canvas.create_window(450, 400, anchor='sw',
                                                                     window=self.use_medkit_button,
                                                                     tags="medkit_button")

        self.use_item_button = tk.Button(self, text='Sell Entered Item\nFrom Inventory',
                                         font='Time_New_Roman 8', command=lambda: self.use_medkit())
        self.use_item_button_window = self.bg_canvas.create_window(650, 400, anchor='sw',
                                                                   window=self.use_item_button, tags="use_item_button")

        self.updateCombatGUI()
        self.mainloop()

    def make_exit(self):
        if self.no_enemy:
            self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 10", command=self.destroy)
            self.exit_button_window = self.bg_canvas.create_window(self.width / 2 - 60, 380,
                                                                   anchor='sw', window=self.exit_button)

    def player_turn(self):
        pass

    def use_medkit(self):
        self.player.use_medkits()
        self.updateCombatGUI()

    def player_grid(self):
        self.bg_canvas.delete("health", "attack", "defense", "medkits")
        self.bg_canvas.create_text(50, self.height - 300, anchor='sw', font=8,
                                   fill="blue", justify="center",
                                   text="Health: " + str(self.player.stats["Health"])
                                   + " / " + str(self.player.stats["Max Health"]), tags="health")
        self.bg_canvas.create_text(50, self.height - 270, anchor='sw', font=8, fill="blue", justify="center",
                                   text="Attack: " + str(self.player.attack), tags="attack")
        self.bg_canvas.create_text(50, self.height - 240, anchor='sw', font=8, fill="blue", justify="center",
                                   text="Defense: " + str(self.player.defense), tags="defense")
        self.bg_canvas.create_text(self.width / 2 + 50, self.height - 240, anchor='sw', font=8, fill="blue", justify="center",
                                   text="Medkits: " + str(self.player.stats["Medkits"]), tags="medkits")

    def updateCombatGUI(self):
        self.player_grid()
