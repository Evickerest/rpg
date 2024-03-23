"""Module containing the MainGUI class.
"""


import tkinter as tk
from PIL import ImageTk, Image
from Classes.GUI.character_gui import CharacterGUI
from Classes.GUI.inventory_gui import InventoryGUI
from Classes.text_printer import TextPrinter

import customtkinter


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
        self.iconbitmap('Images/LevelOne/SpaceShip.ico')
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

    def createButton(self, msg: str, command: callable, x: int, y: int, anchor: str = "sw", font: tuple[str, int] = ("Time New Romans", 20), width=140, height=28, padding=10):
        button = customtkinter.CTkButton(
            self, font=font, text=msg, command=command, corner_radius=0, text_color="black", hover_color="#CCCCCC",
            border_spacing=padding, fg_color="white", width=width, height=height)
        self.bg_canvas.create_window(x, y, anchor=anchor, window=button)

    def createText(self, msg: str, x: int, y: int, font: tuple[str, int] = ("Time New Romans", 20), color: str = 'black', anchor: str = "center", tags: str = None, width: int = None, shadow: bool = False, justify="left"):
        if shadow:
            self.bg_canvas.create_text(x-5, y+5, text=msg, font=font, fill="black", anchor=anchor, tags=tags, width=width)
        self.bg_canvas.create_text(x, y, text=msg, font=font, fill=color, anchor=anchor, tags=tags, width=width, justify=justify)

    def clearGUI(self, img):
        if (self.bg_canvas != None):
            self.bg_canvas.destroy()
        self.bg_canvas = tk.Canvas(self, width=self.screen_width, height=self.screen_height)
        self.bg_canvas.pack(fill='both', expand=True)
        self.img = Image.open(img).resize((self.screen_width, self.screen_height))
        self.image = ImageTk.PhotoImage(self.img)
        self.bg_canvas.create_image(0, 0, image=self.image, anchor='nw')

    def create_intro_screen1(self):
        """Creates the title screen."""
        self.clearGUI('Images/LevelOne/bg2.jpeg')
        self.createText("Are You Ready For a New Adventure?", self.screen_width / 2, self.screen_height / 2, font="Time_New_Roman 45", color='white', shadow=True)
        self.user_name = tk.Label(self, text='User Name:', font='Time_New_Roman 15')
        self.user_name_window = self.bg_canvas.create_window(30, 100, anchor='sw', window=self.user_name, tags="Login_Text")
        self.user_name_entry = tk.Entry(self, font='Time_New_Roman 20')
        self.bg_canvas.create_window(150, 100, anchor='sw', window=self.user_name_entry, tags="Login Button")
        self.createButton("Start Game", self.create_intro_screen2, 30, 200)
        self.createButton("Exit", self.destroy, self.width-200, self.height-100, font=("Time New Romans", 30))

    def create_intro_screen2(self):
        """Destroys the title screen and Creates the game intro screen."""
        self.clearGUI('Images/LevelOne/bg.jpg')
        self.name = self.user_name_entry.get() or "Default"
        self.player.change_name(self.name)
        self.createText(
            "You are a new  Space Janitor sent to"
            " salvage the numerous asteroids and ship"
            " wrecks that pollute space."
            f"\n\n Welcome, {self.name} to being a"
            f" Space Janitor. \nRise to the top.",
            self.width/2, self.height-600, font=("Times New Romans", 20), color="white", shadow=True
        )
        self.createButton("Click Here to Continue", self.create_intro_screen3, self.width/2, self.height-100, anchor="center")

    def printPlayerStats(self):
        self.bg_canvas.delete("stats")
        self.createText( 
            f"{self.player.name}'s Stats:\n\nHealth:{self.player.stats['Health']}/{self.player.stats['Max Health']}" +
            "".join([f'\n\n{stat[0:3]}: {self.player.stats[stat]}' for stat in ["Strength", "Dexterity", "Vitality", "Intelligence"]]) +
            f"\n\nFree Points: {self.player.stats['Stat Points']}\n\nMin: 3, Max: 12",
            self.width/2 - 100, self.height - 500, font=("Time New Romans", 22), color="white", justify="center", tags="stats"
        )

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
        self.printPlayerStats()

    def create_intro_screen3(self):
        """Creates the character creation screen after deleting the introscreen text."""
        self.clearGUI('Images/LevelOne/bg.jpg')
        self.createButton("Start Game", self.create_main_gui, self.width/2, self.height-100, anchor="center")
        self.printPlayerStats()
        
        for i, stat in enumerate(["Strength", "Dexterity", "Vitality", "Intelligence"]):
            cmd = lambda s, n: lambda: self.update_init_stats(s, n)
            self.createButton("-", cmd(stat, -1), self.width/2 - 30, self.height - 600 + 70 * i,
                width=1, height=1, font=("Time New Romans", 20), anchor="center", padding=5
            )
            self.createButton("+", cmd(stat, 1), self.width/2, self.height - 600 + 70 * i,
                width=1, height=1, font=("Time New Romans", 20), anchor="center", padding=5
            )
    
    def create_main_gui(self):
        """Deletes the character screen and makes the main screen.
        """
        self.clearGUI('Images/LevelOne/HallWay.png')

        self.original_image = Image.open('Images/LevelOneMap/Set/Main.jpg').resize((300, 400))
        self.bg = ImageTk.PhotoImage(self.original_image)
        menu_image = Image.open('Images/LevelOne/info_bg.png').resize((300, 200))
        self.menu_bg = ImageTk.PhotoImage(menu_image)

        # Create Canvas and Images
        self.bg_canvas.create_image(self.screen_width - 1280, self.screen_width - 1280, image=self.bg, anchor='nw')
        self.bg_canvas.create_image(self.screen_width - 1280, self.screen_height / 2, image=self.menu_bg, anchor='nw')
        self.createText(f"{self.name}'s Stats", 70, 485, font=("Arial", 20), color="white", anchor="w")
        self.createButton("Character\nDetails", self.open_character_gui, 
            self.screen_width - 1250, self.screen_height - 385, anchor="nw")
        self.createButton("Inventory\nDetails", self.open_inventory_gui, 
            self.screen_width - 1110, self.screen_height - 385, anchor="nw")
        self.createButton("Exit", self.destroy, 10, self.screen_height - 150, anchor="w", font=("Calibri", 20))

        self.createText("\nYou are ready to start cleaning up"
                        " the wreckage. Which wreckage should you"
                        " visit first? Choose a location on the map.\n",
            450, 350, font=("Times New Roman", 15), color="white", anchor="w", tags="game_text", width=500)
        self.createText("Choose Next Location", 1010, 400, font=("Arial", 20), color="white", anchor="w")

        self.start_game()

    def start_game(self):
        """Start the game and load available rooms.
        """
        self.text_printer = TextPrinter(self)
        self.ready = True
        self.map = self.game_handler.get_map()
        self.player = self.game_handler.player
        self.game_handler.enter_room(self.map.get_current_room())
        self.display_buttons()

    def display_buttons(self):
        """Display available rooms to interact with.
        """
        offset = 30

        # Box for map buttons
        self.button_frame = tk.Frame(self.bg_canvas, bg='#0865A0',
                                     borderwidth=3, highlightcolor="white",
                                     highlightthickness=4)
        self.button_frame.place(relwidth=0.20, relheight=0.4,
                                relx=0.78, rely=0.5)

        for adjacent_room in self.map.get_current_room().get_adjacent_rooms():
            test = lambda room: lambda: self.handle_button_input(room)
            button_text = adjacent_room.name  # Button text

            # Determine button color
            # Red means room has been cleared already
            color = "#f69697" if adjacent_room.cleared else "#FFFFFF"

            # Create a button with a lambda function to pass the button_text
            # as an argument
            button = tk.Button(self.button_frame, width=75,
                               font=("Calibri", 15), height=1,
                               text=button_text, command=test(adjacent_room),
                               bg=color)
            button.pack(pady=5)
            offset += 50

    def handle_button_input(self, room):
        """Enters the Room instance and changes the map image to the
         appropriate one.
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
        self.original_image = Image.open(room.map_image_path).resize((300,
                                                                      400))
        self.bg = ImageTk.PhotoImage(self.original_image)
        self.bg_canvas.create_image(self.screen_width - 1280,
                                    self.screen_width - 1280, image=self.bg,
                                    anchor='nw')

    def animate_text(self, text_id, text):
        """Prints text to the MainGUI
    .
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
        self.text_printer.animate_text(f"\n{room} has already been entered.\n",
                                       "game_text", tk.END)

    def enter_chest_room(self, room):
        """Prints text when entering a ChestRoom.
        Args:
            room (ChestRoom): The ChestRoom instance to enter.
        """
        self.text_printer.animate_text(f"\nYou have entered {room} which"
                                       f" contains a chest.\n", "game_text",
                                       tk.END)

    def enter_shop_room(self, room):
        """Prints text when entering a ShopRoom.
        Args:
            room (ShopRoom): The ShopRoom instance to enter.
        """
        self.text_printer.animate_text(f"\nYou have entered {room} which"
                                       f" contains a shop.\n", "game_text",
                                       tk.END)

    def enter_combat_room(self, room):
        """Prints text when entering a CombatRoom.
        Args:
            room (CombatRoom): The CombatRoom instance to enter.
        """
        self.text_printer.animate_text(f"\nYou have entered {room} which"
                                       f" contains combat.\n", "game_text",
                                       tk.END)

    def enter_boss_room(self, room):
        """Prints text when entering a BossRoom.
        Args:
            room (BossRoom): The BossRoom instance to enter.
        """
        self.text_printer.animate_text(f"\n You have entered {room} which is"
                                       f" the boss room.\n", "game_text",
                                       tk.END)

    def exit_boss_room(self):
        """Prints text when exiting a BossRoom.
        """
        if not self.player.living:
            return

        self.text_printer.animate_text("\nCongratulations for beating the"
                                       " boss!\n", "game_text", tk.END)

        # Display End Game Button
        end_game_button = tk.Button(self, font=("Calibri", 16), width=10,
                                    height=2, text="End Game",
                                    command=lambda: self.game_handler.end_game(True))
        self.bg_canvas.create_window(self.width-100, 300, anchor='e',
                                     window=end_game_button)

        # Display Text
        self.bg_canvas.create_text(1010, 235, width=300, font=('Arial', 20),
                                   fill="#FFFFFF", anchor="w",
                                   text="Move to Next Round")

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
            self.text_printer.animate_text(f"\nYou have beaten the enemies"
                                           f" in {room}.\n", "game_text",
                                           tk.END)
        else:
            self.game_handler.end_game(False)

    def open_inventory_gui(self):
        """Opens an InventoryGUI instance.
        """
        if (self.ready and self.map.get_current_room().get_cleared()
                and self.player.living):
            self.ready = False
            self.map.get_current_room().clear_room(False)
            InventoryGUI(self.player, self.map.get_current_room(), self)

    def open_character_gui(self):
        """Opens a CharacterGUI instance.
        """
        print("clicking character")
        print(f"ready: {self.ready}, current: {self.map.get_current_room().get_cleared()}")
        print(f"living: {self.player.living}")
        if (self.ready and self.map.get_current_room().get_cleared()
                and self.player.living):
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
        img = Image.open('Images/LevelOne/GameOver.png').resize((self.screen_width,
                                                        self.screen_height))
        self.img = ImageTk.PhotoImage(img)

        # Create canvas and background
        self.bg_canvas = tk.Canvas(self, width=self.screen_width,
                                   height=self.screen_height)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Heading
        self.bg_canvas.create_text(self.width / 2, self.height / 5 - 100,
                                   font=('Calibri', 50), fill="#ffffff",
                                   justify="center", text="You have died!")
        # Subheading
        self.bg_canvas.create_text(self.width / 2, self.height / 5,
                                   font=('Calibri', 35), fill="#ffffff",
                                   justify="center",
                                   text="You have failed to eradicate all the"
                                   " monsters in the wreckages.")

        # Final stats
        self.bg_canvas.create_text(300, self.height / 4 + 275,
                                   font=('Calibri', 25), fill="#ffffff",
                                   justify="left",
                                   text=f'{self.player.name}\'s Stats:\n\n' +
                                        f'Total Time (s): {total_time}.\n' +
                                        f'Enemies Slain: {enemies_killed}.\n' +
                                        f'Rooms Entered: {rooms_entered}.\n' +
                                        f'Max Health: '
                                        f'{self.player.stats["Max Health"]}.\n'
                                        + f'Strength:'
                                        f' {self.player.stats["Strength"]}.\n'
                                        + f'Dexterity:'
                                        f' {self.player.stats["Dexterity"]}.\n'
                                        + f'Vitality:'
                                        f' {self.player.stats["Vitality"]}.\n'
                                        + f'Intelligence: '
                                        f'{self.player.stats["Intelligence"]}.'
                                   )

        retry_button = tk.Button(self, font=("Calibri", 20), width=8, height=3,
                                 text="Retry?",
                                 command=lambda: self.game_handler.start_new_game())
        self.bg_canvas.create_window(700, self.screen_height / 2, anchor='nw',
                                     window=retry_button, tags="Inv_Screen")

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", font=("Calibri", 20),
                                     width=8, height=3, command=self.destroy)
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
        img = Image.open('Images/LevelOne/GameWon.png').resize((self.screen_width,
                                                       self.screen_height))
        self.img = ImageTk.PhotoImage(img)

        # Create canvas and background
        self.bg_canvas = tk.Canvas(self, width=self.screen_width,
                                   height=self.screen_height)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Heading
        self.bg_canvas.create_text(self.width / 2, self.height / 5 - 100,
                                   font=('Calibri', 50), fill="#ffffff",
                                   justify="center", text="You have won!")
        # Subheading
        self.bg_canvas.create_text(self.width / 2, self.height / 5,
                                   font=('Calibri', 30), fill="#ffffff",
                                   justify="center",
                                   text="You have successfully eradicated all"
                                   " the monsters in the wreckages.")

        # Final stats
        self.bg_canvas.create_text(300, self.height / 4 + 275,
                                   font=('Calibri', 25), fill="#ffffff",
                                   justify="left",
                                   text=f'{self.player.name}\'s Stats:\n\n' +
                                        f'Total Time (s): {total_time}.\n' +
                                        f'Enemies Slain: {enemies_killed}.\n'
                                        + f'Rooms Entered: {rooms_entered}.\n'
                                        + f'Max Health: '
                                        f'{self.player.stats["Max Health"]}.\n'
                                        + f'Strength:'
                                        f' {self.player.stats["Strength"]}.\n'
                                        + f'Dexterity:'
                                        f' {self.player.stats["Dexterity"]}.\n'
                                        + f'Vitality:'
                                        f' {self.player.stats["Vitality"]}.\n'
                                        + f'Intelligence: '
                                        f'{self.player.stats["Intelligence"]}.'
                                   )

        next_map_button = tk.Button(self, font=("Calibri", 20), width=8,
                                    height=3, text="Continue?",
                                    command=lambda: self.game_handler.start_next_map())
        self.bg_canvas.create_window(700, self.screen_height / 2, anchor='nw',
                                     window=next_map_button, tags="Inv_Screen")

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", font=("Calibri", 20),
                                     width=8, height=3, command=self.destroy)
        self.bg_canvas.create_window(550, self.screen_height / 2, anchor='w',
                                     window=self.exit_button)
