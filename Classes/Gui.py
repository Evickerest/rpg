import random
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from Classes.dungeon import *
from Classes.Character import *
from Images import *


class Gui(tk.Tk):

    # Default size of the window.
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size [1]}')  # Window size is provided by user.
        self.minsize(800, 500)  # Minimum size of the window, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.notReady = False

        self.player = None
        self.name = None

        self.a1_details = None
        self.a2_details = None
        self.a3_details = None

        self.a1 = None
        self.a2 = None
        self.a3 = None

        # Widgets
        # self.menu = Menu(self)

        # Customize screen
        self.original_image = Image.open('Images/bg2.jpeg').resize((900, 700))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=900, height=700)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        self.bg_canvas.create_text(400, 250, text="Are You Ready for a New Adventure?",
                                   font="Time_New_Roman 30", fill='white', anchor="center", tags="MainMenu_Text")
        self.user_name = tk.Label(self, text='User Name:', font='Time_New_Roman 15')
        self.user_name_window = self.bg_canvas.create_window(30, 100, anchor='sw', window=self.user_name,
                                                             tags="Login_Text")

        self.user_name_entry = tk.Entry(self, font='Time_New_Roman 20')
        self.bg_canvas.create_window(150, 100, anchor='sw', window=self.user_name_entry,
                                     tags="Login Button")

        self.start_button = tk.Button(self, text="Start", font="Time_New_Roman 20", command=self.game_intro_gui)
        self.start_button_window = self.bg_canvas.create_window(30, 200, anchor='sw', window=self.start_button,
                                                                tags="Start_Button")

        self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 20", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 100, self.height - 100,
                                                               anchor='sw', window=self.exit_button)

        self.mainloop()

    def game_intro_gui(self):
        self.name = "Default Bob"
        if self.user_name_entry.get():
            self.name = self.user_name_entry.get()
        self.bg_canvas.destroy()
        self.original_image = Image.open('Images/bg.jpg').resize((900, 700))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=900, height=700)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')
        self.bg_canvas.create_text(self.width/2, self.height-600, font=20, width=self.width, fill="white",
                                   text="You are a newly recruited Space Janitor sent"
                                   " out to salvage the numerous asteroids and ship wrecks that pollute space."
                                        f"\n\n Welcome, {self.name} to being a Space Janitor."
                                        "\nRise to the top.", tags="intro")
        self.next_text = tk.Button(self, font=5, text="Click here to Continue", command=self.make_player_gui)
        self.bg_canvas.create_window(self.width/2, self.height-100, anchor='center', window=self.next_text)

    def update_init_stats(self, stat: str, amount: int):
        if amount == -1:
            if self.player.stats[stat] > 3:
                self.player.stats[stat] += amount
                self.player.stats["Stat Points"] += -amount
        elif self.player.stats["Stat Points"] >= 1:
            if self.player.stats[stat] < 12:
                self.player.upgradeStats(stat, amount)
        self.player.stats["Health"] = self.player.stats["Max Health"]
        self.player.updateMaxHealth()
        self.bg_canvas.delete("stats")
        self.bg_canvas.create_text(self.width / 2 - 100, self.height - 500, font=25, fill="white", justify="center",
                                   text=self.player.name + "'s Stats" +
                                        "\n\nHealth: " + str(self.player.stats["Health"]) +
                                        "/" + str(self.player.stats["Max Health"]) +
                                        "\n\nStr: " + str(self.player.stats["Strength"]) +
                                        "\n\nDex: " + str(self.player.stats["Dexterity"]) +
                                        "\n\nVit: " + str(self.player.stats["Vitality"]) +
                                        "\n\nInt: " + str(self.player.stats["Intelligence"]) +
                                        "\n\nFree Points: " + str(self.player.stats["Stat Points"]) +
                                        "\n\nMin: 3, Max: 12", tags="stats")


    def make_player_gui(self):
        self.player = Player(str(self.name), {"Strength": 5, "Dexterity": 5, "Vitality": 5,
                                    "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5, "Credits": 0})
        self.bg_canvas.delete("intro")
        self.next_text.config(width=50, text="Start Game", command=self.start_game)
        self.bg_canvas.create_text(self.width / 2 - 100, self.height - 500, font=25, fill="white", justify="center",
                                   text=self.player.name + "'s Stats" +
                                        "\n\nHealth: " + str(self.player.stats["Health"]) +
                                        "/" + str(self.player.stats["Max Health"]) +
                                        "\n\nStr: " + str(self.player.stats["Strength"]) +
                                        "\n\nDex: " + str(self.player.stats["Dexterity"]) +
                                        "\n\nVit: " + str(self.player.stats["Vitality"]) +
                                        "\n\nInt: " + str(self.player.stats["Intelligence"]) +
                                        "\n\nFree Points: " + str(self.player.stats["Stat Points"]) +
                                        "\n\nMin: 3, Max: 12", tags="stats")

        str_down = tk.Button(self, font=5, width=1, height=1, text="-",
                             command=lambda: self.update_init_stats("Strength", -1))
        self.bg_canvas.create_window(self.width / 2 - 30, self.height - 575, anchor='center',
                                     window=str_down)
        str_up = tk.Button(self, font=5, width=1, height=1, text="+",
                             command=lambda: self.update_init_stats("Strength", 1))
        self.bg_canvas.create_window(self.width / 2, self.height - 575, anchor='center',
                                     window=str_up)

        dex_down = tk.Button(self, font=5, width=1, height=1, text="-",
                             command=lambda: self.update_init_stats("Dexterity", -1))
        self.bg_canvas.create_window(self.width / 2 - 30, self.height - 525, anchor='center',
                                     window=dex_down)
        dex_up = tk.Button(self, font=5, width=1, height=1, text="+",
                             command=lambda: self.update_init_stats("Dexterity", 1))
        self.bg_canvas.create_window(self.width / 2, self.height - 525, anchor='center',
                                     window=dex_up)

        vit_down = tk.Button(self, font=5, width=1, height=1, text="-",
                             command=lambda: self.update_init_stats("Vitality", -1))
        self.bg_canvas.create_window(self.width / 2 - 30, self.height - 475, anchor='center',
                                     window=vit_down)
        vit_up = tk.Button(self, font=5, width=1, height=1, text="+",
                             command=lambda: self.update_init_stats("Vitality", 1))
        self.bg_canvas.create_window(self.width / 2, self.height - 475, anchor='center',
                                     window=vit_up)

        int_down = tk.Button(self, font=5, width=1, height=1, text="-",
                             command=lambda: self.update_init_stats("Intelligence", -1))
        self.bg_canvas.create_window(self.width / 2 - 30, self.height - 425, anchor='center',
                                     window=int_down)
        int_up = tk.Button(self, font=5, width=1, height=1, text="+",
                             command=lambda: self.update_init_stats("Intelligence", 1))
        self.bg_canvas.create_window(self.width / 2, self.height - 425, anchor='center',
                                     window=int_up)

    def rooms_update(self):
        """
        Creates three random rooms
        """
        if not Dungeon.ROOM_DETAILS:
            Dungeon.load_room_details()
        self.a1_details = random.choice(Dungeon.ROOM_DETAILS)
        self.a2_details = random.choice(Dungeon.ROOM_DETAILS)
        self.a3_details = random.choice(Dungeon.ROOM_DETAILS)
        while self.a1_details == self.a2_details or self.a1_details == self.a3_details:
            self.a1_details = random.choice(Dungeon.ROOM_DETAILS)
        while self.a2_details == self.a1_details and self.a2_details == self.a3_details:
            self.a2_details = random.choice(Dungeon.ROOM_DETAILS)
        self.a1 = Dungeon(self.a1_details[0], self.a1_details[1])
        self.a2 = Dungeon(self.a2_details[0], self.a2_details[1])
        self.a3 = Dungeon(self.a3_details[0], self.a3_details[1])

    def start_game(self):
        # Clear previous window
        self.bg_canvas.destroy()

        # Create Map Background
        self.original_image = Image.open('Images/mainGameBG.jpg').resize((300, 300))
        self.bg = ImageTk.PhotoImage(self.original_image)

        # Create Canvas and Image
        self.bg_canvas = tk.Canvas(self, width=900, height=700)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(20, 20, image=self.bg, anchor='nw')

        # Creates new rooms
        self.rooms_update()

        # Add Map Buttons
        area1_button = tk.Button(self, font=5, height=1, text=self.a1.name,
                                 command=lambda: self.scene_area_1(self.a1.name))
        self.bg_canvas.create_window(50, 250, anchor='nw', window=area1_button, tags="a1")

        area2_button = tk.Button(self, font=5, height=1, text=self.a2.name,
                                 command=lambda: self.scene_area_1(self.a2.name))
        self.bg_canvas.create_window(165, 165, anchor='nw', window=area2_button, tags="a2")

        area3_button = tk.Button(self, font=5, height=1, text=self.a3.name,
                                 command=lambda: self.scene_area_1(self.a3.name))
        self.bg_canvas.create_window(100, 50, anchor='nw', window=area3_button, tags="a3")

        char_screen_button = tk.Button(self, font=5, height=2, text="Character\nDetails",
                                       command=lambda: CharacterGui(self.player))
        self.bg_canvas.create_window(self.width / 2 - 440, self.height - 300, anchor='nw',
                                     window=char_screen_button, tags="Char_Screen")

        inv_screen_button = tk.Button(self, font=5, height=2, text="Inventory\nDetails",
                                       command=lambda: InventoryGui(self.player))
        self.bg_canvas.create_window(self.width / 2 - 440, self.height - 200, anchor='nw',
                                     window=inv_screen_button, tags="Inv_Screen")

        self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 10", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 50, self.height - 650, anchor='sw',
                                                               window=self.exit_button)

        # Display Stats
        self.stat_grid()
        self.equipment_grid()
        
        self.bg_canvas.create_text(350, 100, width=500, font=30, fill="black", justify="left", anchor="w",
                                   text="\nYou are ready to start cleaning up the wreckage."
                                        " Which wreckage should you visit first?"
                                        " Choose a location on the map.\n", tags="game_text")

    def stat_grid(self):
        self.bg_canvas.delete("stats")
        self.bg_canvas.create_text(self.width / 2 - 300, self.height - 230, font=15, fill="blue", justify="center",
                                   text=self.player.name + "'s Stats" +
                                        "\n\nHealth: " + str(self.player.stats["Health"]) +
                                        "/" + str(self.player.stats["Max Health"]) +
                                        "\n\nStr: " + str(self.player.stats["Strength"]) +
                                        "\n\nDex: " + str(self.player.stats["Dexterity"]) +
                                        "\n\nVit: " + str(self.player.stats["Vitality"]) +
                                        "\n\nInt: " + str(self.player.stats["Intelligence"]) +
                                        "\n\nFree Points: " + str(self.player.stats["Stat Points"]), tags="stats")

    def equipment_grid(self):
        self.bg_canvas.delete("equipment")
        if self.player.equipment:
            self.bg_canvas.create_text(self.width / 2 - 100, self.height - 230, font=15, fill="blue", justify="center",
                                   text="\n\nHead Armor: " + str(self.player.equipment["Head"].stats["name"])
                                        + "\n\nArm Armor: " + str(self.player.equipment["Arms"].stats["name"])
                                        + "\n\nChest Armor: " + str(self.player.equipment["Chest"].stats["name"])
                                        + "\n\nLeg Armor: " + str(self.player.equipment["Legs"].stats["name"])
                                        + "\n\nFoot Armor: " + str(self.player.equipment["Feet"].stats["name"])
                                        + "\n\nWeapon: " + str(self.player.equipment["Weapon"].stats["name"]),
                                   tags="equipment")


    def scene_area_1(self, room_name: str):
        # Creates new rooms
        self.rooms_update()
        self.stat_grid()

        # Animate text to screen
        self.bg_canvas.after_cancel(str(id(self.animate_text)))
        self.bg_canvas.update()
        self.animate_text("game_text", f"\nYou have chosen {room_name}. \n\n"
                                       f"When you arrive in {room_name}, you notice that most"
                                       " of the ship is up and running. What happened to the crew? "
                                       "Choose where to go on the map.\n")
        # Delete map buttons
        self.bg_canvas.delete("a1", "a2", "a3", "Char_Screen", "Inv_Screen", "Exit Button")

        # Add new buttons
        area1_button = tk.Button(self, font=5, height=1, text=self.a1.name,
                                 command=lambda: self.scene_area_1(self.a1.name))
        self.bg_canvas.create_window(50, 250, anchor='nw', window=area1_button, tags="a1")

        area2_button = tk.Button(self, font=5, height=1, text=self.a2.name,
                                 command=lambda: self.scene_area_1(self.a2.name))
        self.bg_canvas.create_window(165, 165, anchor='nw', window=area2_button, tags="a2")

        area3_button = tk.Button(self, font=5, height=1, text=self.a3.name,
                                 command=lambda: self.scene_area_1(self.a3.name))
        self.bg_canvas.create_window(100, 50, anchor='nw', window=area3_button, tags="a3")

        char_screen_button = tk.Button(self, font=5, height=2, text="Character\nDetails",
                                       command=lambda: CharacterGui(self.player))
        self.bg_canvas.create_window(self.width / 2 - 440, self.height - 300, anchor='nw',
                                     window=char_screen_button, tags="Char_Screen")
        inv_screen_button = tk.Button(self, font=5, height=2, text="Inventory\nDetails",
                                      command=lambda: InventoryGui(self.player))
        self.bg_canvas.create_window(self.width / 2 - 440, self.height - 200, anchor='nw',
                                     window=inv_screen_button, tags="Inv_Screen")

        self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 10", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 50, self.height - 650, anchor='sw',
                                                               window=self.exit_button)

    # text_id is the tag of the .create_text object
    # Text contains lines to be printed
    def animate_text(self, text_id, text):
        if self.notReady:
            return
        
        self.toggleReady()

        # TODO: Get this thing to print upwards not downwards
        # Delta is time delay between characters
        delta = 25
        delay = 0
        
        # Change "Ready" state after text is done
        self.bg_canvas.after(delay * (len(text)+1), self.toggleReady())

        for char in text:
            update_text = lambda s=char: self.bg_canvas.insert(text_id, tk.END, s)
            self.bg_canvas.after(delay, update_text)
            delay += delta

    def toggleReady(self):
        self.notReady = not self.notReady
        print(self.notReady)

# ..

class InventoryGui(tk.Tk):
    def __init__(self, player: Player):
        super().__init__()
        self.title("Character Inventory")
        self.geometry(f'{800}x{600}+170+250')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.minsize(self.width, self.height)  # Minimum size of the window, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.player = player

        self.original_image = Image.open('Images/bg2.jpeg').resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height, bg="black")
        self.bg_canvas.pack(fill='both', expand=True)

        self.exit_button = tk.Button(self, text="Close", font="Time_New_Roman 10", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 60, 580,
                                                               anchor='sw', window=self.exit_button)

        self.bg_canvas.create_text(self.width / 2 - 250, self.height - 580, font=10, fill="blue", justify="center",
                                   text=self.player.name + "'s Equipment", tags="equipment_title")
        self.bg_canvas.create_text(self.width / 2 + 250, self.height - 580, font=10, fill="blue", justify="center",
                                   text=self.player.name + "'s Inventory", tags="inventory_title")

        self.unequip_button = tk.Button(self, text='Unequip Entered Item\nFrom Equipment',
                                        font='Time_New_Roman 10', command=lambda: self.removeEquippedItem())
        self.unequip_button_window = self.bg_canvas.create_window(150, 400, anchor='sw',
                                                                  window=self.unequip_button, tags="unequip_button")

        self.equip_button = tk.Button(self, text='Equip Entered Item\nFrom Inventory',
                                      font='Time_New_Roman 10', command=lambda: self.equipItemInventory())
        self.equip_button_window = self.bg_canvas.create_window(350, 400, anchor='sw',
                                                                window=self.equip_button, tags="equip_button")

        self.drop_button = tk.Button(self, text='Drop Entered Item\nFrom Inventory',
                                     font='Time_New_Roman 10', command=lambda: self.dropItemInventory())
        self.drop_button_window = self.bg_canvas.create_window(550, 400, anchor='sw',
                                                               window=self.drop_button, tags="equip_button")

        self.item_entry_text = tk.Label(self, text='Enter Item Below To Start', font='Time_New_Roman 10')
        self.item_entry_text = self.bg_canvas.create_window(150, 450, anchor='sw',
                                                            window=self.item_entry_text, tags="item_entry_text")
        self.item_entry_box = tk.Entry(self, font='Time_New_Roman 12')
        self.bg_canvas.create_window(150, 480, anchor='sw', window=self.item_entry_box, tags="item_entry")

        self.updateInventoryGui()
        self.mainloop()

    def equipment_grid(self):
        self.bg_canvas.delete("equipment")
        if self.player.equipment:
            self.bg_canvas.create_text(self.width / 2 - 250, self.height - 450, font=8, fill="blue", justify="center",
                                   text="\n\n Head Armor:" + str(self.player.equipment["Head"].stats["name"])
                                        + "\n\nArm Armor: " + str(self.player.equipment["Arms"].stats["name"])
                                        + "\n\nChest Armor: " + str(self.player.equipment["Chest"].stats["name"])
                                        + "\n\nLeg Armor: " + str(self.player.equipment["Legs"].stats["name"])
                                        + "\n\nFoot Armor: " + str(self.player.equipment["Feet"].stats["name"])
                                        + "\n\nWeapon: " + str(self.player.equipment["Weapon"].stats["name"]),
                                   tags="equipment")

    def inventory_grid(self):
        self.bg_canvas.delete("inventory")
        self.inventory_text = ""
        if len(self.player.inventory) > 0:
            for item in self.player.inventory:
                if item.stats["type"] == "Weapon":
                    self.inventory_text += ("\n\n" + str(item.stats["name"]) + ": +"
                                            + str(item.stats["damage"]) + " Damage")
                else:
                    self.inventory_text += ("\n\n" + str(item.stats["name"]) + ": +"
                                            + str(item.stats["defense"]) + " Defense")
        else:
            self.inventory_text = "Your Inventory Is Empty"
        self.bg_canvas.create_text(self.width / 2 + 250, self.height - 450, font=10, fill="blue", justify="center",
                                   text=self.inventory_text, tags="inventory")

    def updateInventoryGui(self):
        self.equipment_grid()
        self.inventory_grid()

    def dropItemInventory(self):
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_drop = self.item_entry
            for item in self.player.inventory:
                if item.stats["name"] == item_to_drop:
                    self.player.dropItem(item)
                    self.updateInventoryGui()

    def equipItemInventory(self):
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_equip = self.item_entry
            for item in self.player.inventory:
                if item.stats["name"] == item_to_equip:
                    self.player.equipItem(item)
                    self.updateInventoryGui()

    def removeEquippedItem(self):
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_remove = self.item_entry
            for item in self.player.equipment.values():
                if item.stats["name"] == item_to_remove:
                    self.player.unequipItem(item)
                    self.updateInventoryGui()

    def read_entry_box(self) -> None | str:
        self.item_entry = None
        if self.item_entry_box.get():
            self.item_entry = self.item_entry_box.get()
        return self.item_entry


class CharacterGui(tk.Tk):
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



class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        pass
