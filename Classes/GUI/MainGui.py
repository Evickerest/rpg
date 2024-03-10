"""Module containing the MainGUI class.
"""

import random
import tkinter as tk
# from tkinter import ttk
import tkinter as ttk
from PIL import ImageTk, Image
from Classes.GUI.CharacterGui import CharacterGUI
from Classes.GUI.InventoryGui import InventoryGUI
from Classes.GUI.FightGUI import FightGUI
from Classes.GUI.ShopGUI import ShopGUI
from Classes.Rooms.room import Room
from Classes.textprinter import TextPrinter
from Images import *


class MainGUI(tk.Tk):
    """Class involving the main game window.
    """

    # Default size of the window.
    def __init__(self, player, game_handler):
        """Creates the instance.
        Args:
            player: The player instance
            game_handler: The game_handler instance.
        """
        super().__init__()
        self.title("Spaceship Game")
        self.geometry('1300x900')  # Window size is provided by user.
        self.minsize(800, 500)  # Minimum size of the window, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.screen_width = 1300
        self.screen_height = 900
        self.original_image = None
        self.bg = None
        self.bg_canvas = None
        self.user_name = None
        self.user_name_entry = None
        self.user_name_window = None
        self.start_button = None
        self.start_button_window = None
        self.exit_button = None
        self.exit_button_window = None
        self.text_printer = None
        self.next_text = None
        self.background_image = None
        self.backg = None
        self.button_frame = None
        self.img = None
        self.menu_bg = None
        self.map = None

        self.player = player
        self.name = None
        self.game_handler = game_handler
        self.game_handler.set_gui(self)
        self.ready = True

        self.create_intro_screen1()
        self.mainloop()
      
    def create_intro_screen1(self):
        """Creates the title screen.
        """
        self.original_image = Image.open('Images/bg2.jpeg').resize((self.screen_width,
                                                                    self.screen_height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.screen_width, height=self.screen_height)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        self.bg_canvas.create_text(self.screen_width / 2, self.screen_height / 2,
                                   text="Are You Ready For a New Adventure?",
                                   font="Time_New_Roman 45", fill='#041A00',
                                   anchor="center", tags="MainMenu_Text")
        self.bg_canvas.create_text(self.screen_width / 2, self.screen_height / 2,
                                   text="Are You Ready For a New Adventure?",
                                   font="TTime_New_Roman 44", fill='white',
                                   anchor="center", tags="MainMenu_Text")
        self.user_name = tk.Label(self, text='User Name:', font='Time_New_Roman 15')
        self.user_name_window = self.bg_canvas.create_window(30, 100, anchor='sw',
                                                             window=self.user_name,
                                                             tags="Login_Text")

        self.user_name_entry = tk.Entry(self, font='Time_New_Roman 20')
        self.bg_canvas.create_window(150, 100, anchor='sw', window=self.user_name_entry,
                                     tags="Login Button")

        self.start_button = tk.Button(self, text="Start", font="Time_New_Roman 20",
                                      command=self.create_intro_screen2)
        self.start_button_window = self.bg_canvas.create_window(30, 200, anchor='sw',
                                                                window=self.start_button,
                                                                tags="Start_Button")

        self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 20",
                                     command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 100, self.height - 100,
                                                               anchor='sw',
                                                               window=self.exit_button)
    
    def create_intro_screen2(self):
        """Destroys the title screen and Creates the game intro screen.
        """
        self.name = "Default"
        if self.user_name_entry.get():
            self.name = self.user_name_entry.get()
            self.player.change_name(self.name)

        self.bg_canvas.destroy()
        self.original_image = Image.open('Images/bg.jpg').resize((self.screen_width,
                                                                  self.screen_height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        # Make text printer object
        self.text_printer = TextPrinter(self)

        self.bg_canvas = tk.Canvas(self, width=self.screen_width, height=self.screen_height)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')
        self.bg_canvas.create_text(self.width/2, self.height-600, font="Time_New_Roman 22",
                                   width=self.width, fill="white",
                                   text="You are a new  Space Janitor sent to salvage the numerous"
                                   " asteroids and ship wrecks that pollute space."
                                   f"\n\n Welcome, {self.name} to being a Space Janitor."
                                   "\nRise to the top.", tags="intro")
        self.next_text = tk.Button(self, font=5, text="Click here to Continue",
                                   command=self.create_intro_screen3)
        self.bg_canvas.create_window(self.width/2, self.height-100, anchor='center',
                                     window=self.next_text)

    def create_intro_screen3(self):
        """Creates the character creation screen after deleting the intro screen text.
        """
        self.bg_canvas.delete("intro")
        self.next_text.config(width=50, text="Start Game", command=self.create_main_gui)
        self.bg_canvas.create_text(self.width / 2 - 100, self.height - 500,
                                   font="Time_New_Roman 22", fill="white", justify="center",
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
        
    def update_init_stats(self, stat: str, amount: int):
        """Method that affects the Player's stats.
        Args:
            stat (str): The stat to change.
            amount (int): How much to change the stat by.
             Increases only if the Player has unassigned Stat Points.
        """
        if amount == -1:
            if self.player.stats[stat] > 3:
                self.player.stats[stat] += amount
                self.player.stats["Stat Points"] += -amount
        elif self.player.stats["Stat Points"] >= 1:
            if self.player.stats[stat] < 12:
                self.player.upgrade_stats(stat, amount)
        self.player.update_max_health()
        self.player.stats["Health"] = self.player.stats["Max Health"]
        self.bg_canvas.delete("stats")
        self.bg_canvas.create_text(self.width / 2 - 100, self.height - 500, font=25,
                                   fill="white", justify="center",
                                   text=self.player.name + "'s Stats" +
                                   "\n\nHealth: " + str(self.player.stats["Health"]) +
                                   "/" + str(self.player.stats["Max Health"]) +
                                   "\n\nStr: " + str(self.player.stats["Strength"]) +
                                   "\n\nDex: " + str(self.player.stats["Dexterity"]) +
                                   "\n\nVit: " + str(self.player.stats["Vitality"]) +
                                   "\n\nInt: " + str(self.player.stats["Intelligence"]) +
                                   "\n\nFree Points: " + str(self.player.stats["Stat Points"]) +
                                   "\n\nMin: 3, Max: 12", tags="stats")

    def create_main_gui(self):
        """Deletes the character screen and makes the main screen.
        """
        # Clear previous window
        self.bg_canvas.destroy()

        # Create Map Background
        self.background_image = Image.open('Images/HallWay.png').resize((self.screen_width,
                                                                         self.screen_height))
        self.backg = ImageTk.PhotoImage(self.background_image)

        self.original_image = Image.open('Map/Set/Main.jpg').resize((300, 400))
        self.bg = ImageTk.PhotoImage(self.original_image)

        # Create Menu Background
        menu_image = Image.open('Images/info_bg.png').resize((300, 200))
        self.menu_bg = ImageTk.PhotoImage(menu_image)

        self.bg_canvas = tk.Canvas(self, width=self.screen_width, height=self.screen_height)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.backg, anchor='nw')
      
        # Create Canvas and Images
        self.bg_canvas.create_image(self.screen_width - 1280, self.screen_width - 1280,
                                    image=self.bg, anchor='nw')
        self.bg_canvas.create_image(self.screen_width - 1280, (self.screen_height / 2),
                                    image=self.menu_bg, anchor='nw')

        # Name's Stat text
        self.bg_canvas.create_text(70, 485, width=300, font=('Arial', 20), fill="#FFFFFF",
                                   anchor="w", text=f"{self.name}'s Stats")

        # Character Detail Button
        char_screen_button = tk.Button(self, font=("Calibri", 16), width=8, height=3,
                                       text="Character\nDetails",
                                       command=lambda: self.open_character_gui())
        self.bg_canvas.create_window(self.screen_width - 1250, self.screen_height - 385,
                                     anchor='nw', window=char_screen_button, tags="Char_Screen")

        # Inventory Detail Button
        inv_screen_button = tk.Button(self, font=("Calibri", 16), width=8, height=3,
                                      text="Inventory\nDetails",
                                      command=lambda: self.open_inventory_gui())
        self.bg_canvas.create_window(self.screen_width - 1110, self.screen_height - 385,
                                     anchor='nw', window=inv_screen_button, tags="Inv_Screen")
        
        # For testing purposes
        # beat_boss_test = tk.Button(self, font=("Calibri", 16), width=8, height=3,
        #                            text="Beat\nBoss",
        #                            command=lambda: self.exit_boss_room())
        # self.bg_canvas.create_window(600, 700, anchor='nw', window=beat_boss_test)

        # lost_test = tk.Button(self, font=("Calibri", 16), width=8, height=3, text="Lose",
        #                       command=lambda: self.game_handler.end_game(False))
        # self.bg_canvas.create_window(700, 700, anchor='nw', window=lost_test)

        # win_test = tk.Button(self, font=("Calibri", 16), width=8, height=3, text="Win",
        #                      command=lambda: self.game_handler.end_game(True))
        # self.bg_canvas.create_window(800, 700, anchor='nw', window=win_test)

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", font="Calibri 20", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(10, self.screen_height - 150,
                                                               anchor='w', window=self.exit_button)
        
        self.bg_canvas.create_text(450, 350, width=500, font=('Time_New_Roman', 15),
                                   fill="#FFFFFF", justify="left", anchor="w",
                                   text="\nYou are ready to start cleaning up the wreckage."
                                   " Which wreckage should you visit first?"
                                   " Choose a location on the map.\n", tags="game_text")

        self.bg_canvas.create_text(1010, 400, width=300, font=('Arial', 20), fill="#FFFFFF",
                                   anchor="w", text="Choose Next Location")

        self.start_game()

    def start_game(self):
        """Start the game and load available rooms.
        """
        self.map = self.game_handler.get_map()
        self.game_handler.enter_room(self.map.get_current_room())
        self.display_buttons()

    def display_buttons(self):
        """Display available rooms to interact with.
        """
        offset = 30

        # Box for map buttons
        self.button_frame = tk.Frame(self.bg_canvas, bg='#0865A0', borderwidth=3,
                                     highlightcolor="white", highlightthickness=4)
        self.button_frame.place(relwidth=0.20, relheight=0.4, relx=0.78, rely=0.5)
        
        for adjacentRoom in self.map.get_current_room().get_adjacent_rooms():
            test = lambda room: lambda: self.handle_button_input(room)
            button_text = adjacentRoom.name  # Button text

            # Determine button color
            # Red means room has been cleared already
            color = "#f69697" if adjacentRoom.cleared else "#FFFFFF"

            # Create a button with a lambda function to pass the button_text as an argument
            button = tk.Button(self.button_frame, width=75, font=("Calibri", 15), height=1, 
                               text=button_text, command=test(adjacentRoom),
                               bg=color)
            button.pack(pady=5)
            offset += 50
            
    def handle_button_input(self, room):
        """Enters the Room instance and changes the map image to the appropriate one.
        Args:
            room (Room): The Room instance just entered.
        """
        if self.ready and self.player.living and self.map.current_room.cleared:
            self.change_map_image(room)
            self.game_handler.enter_room(room)

    def change_map_image(self, room):
        """Changes the minimap to the new image.
        Args:
            room (Room): The Room instance with the associated image.
        """
        self.original_image = Image.open(room.map_image_path).resize((300, 400))
        self.bg = ImageTk.PhotoImage(self.original_image)
        self.bg_canvas.create_image(self.screen_width - 1280, self.screen_width - 1280,
                                    image=self.bg, anchor='nw')
     
    def animate_text(self, text_id, text):
        """Prints text to the MainGUI.
        Args:
            text_id (str): The text_box to print to.
            text (str): The text to print.
        """
        self.text_printer.animate_text(text, text_id, tk.END)

    def enter_repeated_room(self, room):
        """Prints text when entering a previously cleared room.
        Args:
            room (Room): The already cleared room.
        """
        self.text_printer.animate_text(f"\n{room} has already been entered.\n", "game_text", tk.END)

    def enter_chest_room(self, room):
        """Prints text when entering a ChestRoom.
        Args:
            room (ChestRoom): The ChestRoom instance to enter.
        """
        self.text_printer.animate_text(f"\nYou have entered {room} which contains a chest.\n",
                                       "game_text", tk.END)
        
    def enter_shop_room(self, room):
        """Prints text when entering a ShopRoom.
        Args:
            room (ShopRoom): The ShopRoom instance to enter.
        """
        self.text_printer.animate_text(f"\nYou have entered {room} which contains a shop.\n",
                                       "game_text", tk.END)
      
    def enter_combat_room(self, room):
        """Prints text when entering a CombatRoom.
        Args:
            room (CombatRoom): The CombatRoom instance to enter.
        """
        self.text_printer.animate_text(f"\nYou have entered {room} which contains combat.\n",
                                       "game_text", tk.END)

    def enter_boss_room(self, room):
        """Prints text when entering a BossRoom.
        Args:
            room (BossRoom): The BossRoom instance to enter.
        """
        self.text_printer.animate_text(f"\n You have entered {room} which is the boss room.\n",
                                       "game_text", tk.END)

    def exit_boss_room(self):
        """Prints text when exiting a BossRoom.
        """
        if not self.player.living: return

        self.text_printer.animate_text(f"\nCongratulations for beating the boss!\n",
                                       "game_text", tk.END)

        # Display End Game Button
        end_game_button = tk.Button(self, font=("Calibri", 16), width=10, height=2, text="End Game",
                                    command=lambda: self.game_handler.end_game(True))
        self.bg_canvas.create_window(self.width-100, 300, anchor='e', window=end_game_button)

        # Display Text
        self.bg_canvas.create_text(1010, 235, width=300, font=('Arial', 20), fill="#FFFFFF",
                                   anchor="w", text="Move to Next Round")
        
    def exit_room(self, room):
        """Prints text when exiting a Room.
        Args:
            room (Room): The Room instance that was just cleared.
        """
        self.text_printer.animate_text(f"\nYou have exited {room}.\n",
                                       "game_text", tk.END)
    
    def exit_combat_room(self, room):
        """Prints text when exiting a CombatRoom.
        Args:
            room (CombatRoom): The CombatRoom instance that was just cleared.
        """
        if self.player.living:
            self.text_printer.animate_text(f"\nYou have beaten the enemies in {room}.\n",
                                           "game_text", tk.END)
        else:
            self.game_handler.end_game(False)
            # self.text_printer.animate_text(f"\nYou have lost to the enemies in {room}.\n",
            #                                "game_text", tk.END)
            # # Display End Game Button
            # end_game_button = tk.Button(self, font=("Calibri", 16), width=10, height=2, text="End Game",
            #                             command=lambda: self.game_handler.end_game(False))
            # self.bg_canvas.create_window(self.width - 100, 300, anchor='e', window=end_game_button)

    def open_inventory_gui(self):
        """Opens an InventoryGUI instance.
        """
        if self.ready and self.map.get_current_room().get_cleared() and self.player.living:
            self.ready = False
            self.map.get_current_room().clear_room(False)
            InventoryGUI(self.player, self.map.get_current_room(), self)

    def open_character_gui(self):
        """Opens a CharacterGUI instance.
        """
        if self.ready and self.map.get_current_room().get_cleared() and self.player.living:
            self.ready = False
            self.map.get_current_room().clear_room(False)
            CharacterGUI(self.player, self.map.get_current_room(), self)

    def display_game_lost_gui(self, total_time, enemies_killed, rooms_entered):
        """The screen that shows when you lose the game.
        Args:
            total_time (int): The total time spent.
            enemies_killed (int): The number of enemies killed.
            rooms_entered (int): The number of rooms entered.
        """
        # Clear previous window
        self.bg_canvas.destroy()

        # Import Map Background
        img = Image.open('Images/GameOver.png').resize((self.screen_width, self.screen_height))
        self.img = ImageTk.PhotoImage(img)

        # Create canvas and background
        self.bg_canvas = tk.Canvas(self, width=self.screen_width, height=self.screen_height)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.img, anchor='nw')
      
        # Heading
        self.bg_canvas.create_text(self.width / 2, self.height / 5 - 100, font=('Calibri', 50),
                                   fill="#ffffff", justify="center",
                                   text="You have died!")
        # Subheading
        self.bg_canvas.create_text(self.width / 2, self.height / 5, font=('Calibri', 35),
                                   fill="#ffffff", justify="center",
                                   text="You have failed to eradicate all the monsters"
                                        " in the wreckages.")
    
        # Final stats
        self.bg_canvas.create_text(300, self.height / 4 + 275, font=('Calibri', 25),
                                   fill="#ffffff", justify="left",
                                   text=f'{self.player.name}\'s Stats:\n\n' + 
                                        f'Total Time (s): {total_time}.\n' +
                                        f'Enemies Slain: {enemies_killed}.\n' +
                                        f'Rooms Entered: {rooms_entered}.\n' +
                                        f'Max Health: {self.player.stats["Max Health"]}.\n' +
                                        f'Strength: {self.player.stats["Strength"]}.\n' +
                                        f'Dexterity: {self.player.stats["Dexterity"]}.\n' +
                                        f'Vitality: {self.player.stats["Vitality"]}.\n' +
                                        f'Intelligence: {self.player.stats["Intelligence"]}.'
                                   )
        
        retry_button = tk.Button(self, font=("Calibri", 20), width=8, height=3, text="Retry?",
                                 command=lambda: self.game_handler.start_new_game())
        self.bg_canvas.create_window(700, self.screen_height / 2,
                                     anchor='nw', window=retry_button, tags="Inv_Screen")

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", font=("Calibri", 20), width=8, height=3,
                                     command=self.destroy)
        self.bg_canvas.create_window(550, self.screen_height / 2, anchor='w',
                                     window=self.exit_button)
                
    def display_game_won_gui(self, total_time, enemies_killed, rooms_entered):
        """The screen that shows when you win the game.
        Args:
            total_time (ChestRoom): The ChestRoom instance to enter.
            enemies_killed (int): The number of enemies killed.
            rooms_entered (int): The number of rooms entered.
        """
        # Clear previous window
        self.bg_canvas.destroy()

        # Import Map Background
        img = Image.open('Images/GameWon.png').resize((self.screen_width, self.screen_height))
        self.img = ImageTk.PhotoImage(img)

        # Create canvas and background
        self.bg_canvas = tk.Canvas(self, width=self.screen_width, height=self.screen_height)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.img, anchor='nw')
      
        # Heading
        self.bg_canvas.create_text(self.width / 2, self.height / 5 - 100, font=('Calibri', 50),
                                   fill="#ffffff", justify="center", text="You have won!")
        # Subheading
        self.bg_canvas.create_text(self.width / 2, self.height / 5, font=('Calibri', 30),
                                   fill="#ffffff", justify="center",
                                   text="You have successfully eradicated all the monsters"
                                        " in the wreckages.")
    
        # Final stats
        self.bg_canvas.create_text(300, self.height / 4 + 275, font=('Calibri', 25),
                                   fill="#ffffff", justify="left",
                                   text=f'{self.player.name}\'s Stats:\n\n' + 
                                        f'Total Time (s): {total_time}.\n' +
                                        f'Enemies Slain: {enemies_killed}.\n' +
                                        f'Rooms Entered: {rooms_entered}.\n' +
                                        f'Max Health: {self.player.stats["Max Health"]}.\n' +
                                        f'Strength: {self.player.stats["Strength"]}.\n' +
                                        f'Dexterity: {self.player.stats["Dexterity"]}.\n' +
                                        f'Vitality: {self.player.stats["Vitality"]}.\n' +
                                        f'Intelligence: {self.player.stats["Intelligence"]}.'
                                   )

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", font=("Calibri", 20), width=8, height=3,
                                     command=self.destroy)
        self.bg_canvas.create_window(550, self.screen_height / 2, anchor='w', window=self.exit_button)
