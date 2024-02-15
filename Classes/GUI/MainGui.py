import random
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from Classes.GUI.CharacterGui import CharacterGui
from Classes.GUI.InventoryGui import InventoryGui
from Classes.dungeon import *
from Images import *
from Classes.TextPrinter import *


class MainGui(tk.Tk):

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

        # Make text printer object
        self.textPrinter = TextPrinter(self)

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

        # Create Menu Background
        menu_image = Image.open('Images/info_bg.png').resize((300, 300))
        self.menu_bg = ImageTk.PhotoImage(menu_image)
    

        #Create backgroung
        self.bg_canvas = tk.Canvas(self, width=900, height=700)
        self.bg_canvas.configure(bg='#34557A')
        
        # Create Canvas and Images
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(20, 20, image=self.bg, anchor='nw')
        self.bg_canvas.create_image(20,350, image=self.menu_bg, anchor='nw')

        # Creates new rooms
        self.rooms_update()

        # Add Map Buttons

        # Scene 1 Button
        area1_button = tk.Button(self, font=5, height=1, text=self.a1.name,
                                 command=lambda: self.scene_area_1(self.a1.name))
        self.bg_canvas.create_window(50, 250, anchor='nw', window=area1_button, tags="a1")

        # Scene 2 Button
        area2_button = tk.Button(self, font=5, height=1, text=self.a2.name,
                                 command=lambda: self.scene_area_1(self.a2.name))
        self.bg_canvas.create_window(165, 165, anchor='nw', window=area2_button, tags="a2")

        # Scene 3 Button
        area3_button = tk.Button(self, font=5, height=1, text=self.a3.name,
                                 command=lambda: self.scene_area_1(self.a3.name))
        self.bg_canvas.create_window(100, 50, anchor='nw', window=area3_button, tags="a3")

        # Character Detail Button
        char_screen_button = tk.Button(self, font=5, height=2, text="Character\nDetails",
                                       command=lambda: CharacterGui(self.player))
        self.bg_canvas.create_window(50, 475, anchor='nw',
                                     window=char_screen_button, tags="Char_Screen")

        # Inventory Detail Button
        inv_screen_button = tk.Button(self, font=5, height=2, text="Inventory\nDetails",
                                       command=lambda: InventoryGui(self.player))
        self.bg_canvas.create_window(160, 475, anchor='nw',
                                     window=inv_screen_button, tags="Inv_Screen")

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 10", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 50, self.height - 650, anchor='sw',
                                                               window=self.exit_button)

        # Display Stats
        self.stat_grid()
        self.equipment_grid()
        
        self.bg_canvas.create_text(350, 350, width=500, font=30, fill="black", justify="left", anchor="w",
                                   text="\nYou are ready to start cleaning up the wreckage."
                                        " Which wreckage should you visit first?"
                                        " Choose a location on the map.\n", tags="game_text")

    def stat_grid(self):
        self.bg_canvas.delete("stats")
        # self.bg_canvas.create_text(self.width / 2 - 300, self.height - 230, font=15, fill="white", justify="center",
        #                            text=self.player.name + "'s Stats" +
        #                                 "\n\nHealth: " + str(self.player.stats["Health"]) +
        #                                 "/" + str(self.player.stats["Max Health"]) +
        #                                 "\n\nStr: " + str(self.player.stats["Strength"]) +
        #                                 "\n\nDex: " + str(self.player.stats["Dexterity"]) +
        #                                 "\n\nVit: " + str(self.player.stats["Vitality"]) +
        #                                 "\n\nInt: " + str(self.player.stats["Intelligence"]) +
        #     
        #                             "\n\nFree Points: " + str(self.player.stats["Stat Points"]), tags="stats")

        # To much info on screen, there is already a window that can display that info

        self.bg_canvas.create_text(160,400, font=15, fill="white", justify="left", 
                                   text=self.player.name + "'s Stats" +
                                        "\n\nHealth: " + str(self.player.stats["Health"]), tags="stats")



    def equipment_grid(self):
        # self.bg_canvas.delete("equipment")
        # if self.player.equipment:
        #     self.bg_canvas.create_text(self.width / 2 - 100, self.height - 230, font=15, fill="blue", justify="center",
        #                            text="\n\nHead Armor: " + str(self.player.equipment["Head"].stats["name"])
        #                                 + "\n\nArm Armor: " + str(self.player.equipment["Arms"].stats["name"])
        #                                 + "\n\nChest Armor: " + str(self.player.equipment["Chest"].stats["name"])
        #                                 + "\n\nLeg Armor: " + str(self.player.equipment["Legs"].stats["name"])
        #                                 + "\n\nFoot Armor: " + str(self.player.equipment["Feet"].stats["name"])
        #                                 + "\n\nWeapon: " + str(self.player.equipment["Weapon"].stats["name"]),
        #                            tags="equipment")

        # To much info on screen, there is already a window that can display that info
        pass


    def scene_area_1(self, room_name: str):
        # If text is still printing, don't allow input
        if self.textPrinter.isTextReady() == False:
            return


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


        # Character Detail Button
        char_screen_button = tk.Button(self, font=5, height=2, text="Character\nDetails",
                                       command=lambda: CharacterGui(self.player))
        self.bg_canvas.create_window(50, 475, anchor='nw',
                                     window=char_screen_button, tags="Char_Screen")

        # Inventory Detail Button
        inv_screen_button = tk.Button(self, font=5, height=2, text="Inventory\nDetails",
                                       command=lambda: InventoryGui(self.player))
        self.bg_canvas.create_window(160, 475, anchor='nw',
                                     window=inv_screen_button, tags="Inv_Screen")
        
        self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 10", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 50, self.height - 650, anchor='sw',
                                                               window=self.exit_button)

    # text_id is the tag of the .create_text object
    # Text contains lines to be printed
    def animate_text(self, text_id, text):
       self.textPrinter.animate_text(text,text_id,tk.END)
