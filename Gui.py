import random
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from character import *
from dungeon import *
import time
from threading import *


class Gui(tk.Tk):

    # Default size of the window.
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size [1]}')  # Window size is provided by user.
        self.minsize(800, 500)  # Minimum size of the window, can be maximized.
        self.iconbitmap('SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

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
        self.original_image = Image.open('bg2.jpeg').resize((900, 700))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=900, height=700)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        self.bg_canvas.create_text(400, 250, text="Are You Ready for a New Adventure?",
                                   font="Time_New_Roman 30", fill='white', anchor="center")
        self.user_name = tk.Label(self, text='User Name:', font='Time_New_Roman 15')
        self.user_name_window = self.bg_canvas.create_window(30, 100, anchor='sw', window=self.user_name)

        self.user_name_entry = tk.Entry(self, font='Time_New_Roman 20')
        self.bg_canvas.create_window(150, 100, anchor='sw', window=self.user_name_entry)

        self.start_button = tk.Button(self, text="Start", font="Time_New_Roman 20", command=self.game_intro_gui)
        self.start_button_window = self.bg_canvas.create_window(30, 200, anchor='sw', window=self.start_button)

        self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 20", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(30, 650, anchor='sw', window=self.exit_button)

        self.mainloop()

    def game_intro_gui(self):
        self.name = "Default Bob"
        if self.user_name_entry.get():
            self.name = self.user_name_entry.get()
        self.bg_canvas.destroy()
        self.original_image = Image.open('bg.jpg').resize((900, 700))
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

    def update_make_player_gui(self):
        self.bg_canvas.delete("init_stats")
        self.bg_canvas.create_text(self.width/2-100, self.height-500, font=25, fill="white", justify="center",
                                   text=f"{self.player.name}'s Stats\n\n"
                                        f"Str: {self.player.strength}\n\n"
                                        f"Dex: {self.player.dexterity}\n\n"
                                        f"Vit: {self.player.vitality}\n\n"
                                        f"Int: {self.player.intelligence}\n\n"
                                        f"Free Points: {self.player.stats}\n\n", tags="init_stats")

    def add_str(self):
        if self.player.stats > 0:
            self.player.strength = 1
            self.player.stats = -1
            self.update_make_player_gui()

    def sub_str(self):
        if self.player.strength > 1:
            self.player.strength = -1
            self.player.stats = 1
            self.update_make_player_gui()

    def add_dex(self):
        if self.player.stats > 0:
            self.player.dexterity = 1
            self.player.stats = -1
            self.update_make_player_gui()

    def sub_dex(self):
        if self.player.dexterity > 1:
            self.player.dexterity = -1
            self.player.stats = 1
            self.update_make_player_gui()

    def add_vit(self):
        if self.player.stats > 0:
            self.player.vitality = 1
            self.player.stats = -1
            self.update_make_player_gui()

    def sub_vit(self):
        if self.player.vitality > 1:
            self.player.vitality = -1
            self.player.stats = 1
            self.update_make_player_gui()

    def add_int(self):
        if self.player.stats > 0:
            self.player.intelligence = 1
            self.player.stats = -1
            self.update_make_player_gui()

    def sub_int(self):
        if self.player.intelligence > 1:
            self.player.intelligence = -1
            self.player.stats = 1
            self.update_make_player_gui()

    def make_player_gui(self):
        self.player = Player(f"{self.name}")
        self.bg_canvas.delete("intro")
        self.next_text.config(width=50, text="Start Game", command=self.start_game)
        self.bg_canvas.create_text(self.width/2-100, self.height-500, font=30, fill="white", justify="center",
                                   text=f"{self.player.name}'s Stats\n\n"
                                        f"Str: {self.player.strength}\n\n"
                                        f"Dex: {self.player.dexterity}\n\n"
                                        f"Vit: {self.player.vitality}\n\n"
                                        f"Int: {self.player.intelligence}\n\n"
                                        f"Free Points: {self.player.stats}\n\n", tags="init_stats")

        str_down = tk.Button(self, font=5, width=1, height=1, text="-", command=self.sub_str)
        self.bg_canvas.create_window(self.width / 2 - 60, self.height - 595, anchor='center',
                                     window=str_down)
        str_up = tk.Button(self, font=5, width=1, height=1, text="+", command=self.add_str)
        self.bg_canvas.create_window(self.width/2-30, self.height-595, anchor='center',
                                     window=str_up)

        dex_down = tk.Button(self, font=5, width=1, height=1, text="-", command=self.sub_dex)
        self.bg_canvas.create_window(self.width / 2 - 60, self.height - 545, anchor='center',
                                     window=dex_down)
        dex_up = tk.Button(self, font=5, width=1, height=1, text="+", command=self.add_dex)
        self.bg_canvas.create_window(self.width / 2 - 30, self.height - 545, anchor='center',
                                     window=dex_up)

        vit_down = tk.Button(self, font=5, width=1, height=1, text="-", command=self.sub_vit)
        self.bg_canvas.create_window(self.width / 2 - 60, self.height - 495, anchor='center',
                                     window=vit_down)
        vit_up = tk.Button(self, font=5, width=1, height=1, text="+", command=self.add_vit)
        self.bg_canvas.create_window(self.width / 2 - 30, self.height - 495, anchor='center',
                                     window=vit_up)

        int_down = tk.Button(self, font=5, width=1, height=1, text="-", command=self.sub_int)
        self.bg_canvas.create_window(self.width / 2 - 60, self.height - 445, anchor='center',
                                     window=int_down)
        int_up = tk.Button(self, font=5, width=1, height=1, text="+", command=self.add_int)
        self.bg_canvas.create_window(self.width / 2 - 30, self.height - 445, anchor='center',
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
        self.original_image = Image.open('mainGameBG.jpg').resize((300, 300))
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

        # Display Stats
        self.bg_canvas.create_text(170, 500, font=30, fill="black", justify="center",
                                   text=f"{self.player.name}'s Stats\n\n"
                                        f"Str: {self.player.strength}\n\n"
                                        f"Dex: {self.player.dexterity}\n\n"
                                        f"Vit: {self.player.vitality}\n\n"
                                        f"Int: {self.player.intelligence}\n\n", tags="game_stats")
        
        self.bg_canvas.create_text(350, 100, width=500, font=30, fill="black", justify="left", anchor="w",
                                   text="\nYou are ready to start cleaning up the wreckage."
                                        " Which wreckage should you visit first?"
                                        " Choose a location on the map.\n", tags="game_text")
       
    def scene_area_1(self, room_name: str):
        # Creates new rooms
        self.rooms_update()

        # Animate text to screen
        self.bg_canvas.after_cancel(str(id(self.animate_text)))
        self.bg_canvas.update()
        self.animate_text("game_text", f"\nYou have chosen {room_name}. \n\n"
                                       f"When you arrive in {room_name}, you notice that most"
                                       " of the ship is up and running. What happened to the crew? "
                                       "Choose where to go on the map.\n")
        # Delete map buttons
        self.bg_canvas.delete("a1", "a2", "a3")

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

    # text_id is the tag of the .create_text object
    # Text contains lines to be printed
    def animate_text(self, text_id, text):
        # Stolen from stackoverflow
        # Delta controls rate of range (Milliseconds)

        # TODO: Get this thing to print upwards not downwards
        delta = 25
        delay = 0
        for char in text:
            update_text = lambda s=char: self.bg_canvas.insert(text_id, tk.END, s)
            self.bg_canvas.after(delay, update_text)
            delay += delta
        
    







# ..


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        pass


if __name__ == "__main__":
    Gui("SpaceShip Game", (900, 700))
