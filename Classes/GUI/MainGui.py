import random
import tkinter as tk
# from tkinter import ttk
import tkinter as ttk
from PIL import ImageTk, Image
from Classes.GUI.CharacterGui import CharacterGUI
from Classes.GUI.InventoryGui import InventoryGUI
from Classes.GUI.FightGUI import FightGUI
from Classes.GUI.ShopGUI import ShopGUI

from Classes.Rooms.Room import *
from Images import *
from Classes.TextPrinter import *


class MainGUI(tk.Tk):

    # Default size of the window.
    def __init__(self, player, gameHandler):
        super().__init__()
        self.title("Spaceship Game")
        self.geometry('1300x900')  # Window size is provided by user.
        self.minsize(800, 500)  # Minimum size of the window, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.screenWidth = 1300
        self.screenHeight = 900


        self.player = player
        self.name = None
        self.gameHandler = gameHandler
        self.gameHandler.setGUI(self)
        self.displayed_buttons = []
        self.ready = True


        self.createIntroScreen1()
        self.mainloop()
        #self.display_buttons() 



    def createIntroScreen1(self):
        self.original_image = Image.open('Images/bg2.jpeg').resize((self.screenWidth, self.screenHeight))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.screenWidth, height=self.screenHeight)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        self.bg_canvas.create_text(self.screenWidth /2, self.screenHeight / 2, text="Are You Ready For a New Adventure?",
                                   font="Time_New_Roman 45", fill='#041A00', anchor="center", tags="MainMenu_Text")
        self.bg_canvas.create_text(self.screenWidth / 2, self.screenHeight / 2,
                                   text="Are You Ready For a New Adventure?",
                                   font="TTime_New_Roman 44", fill='white', anchor="center", tags="MainMenu_Text")
        self.user_name = tk.Label(self, text='User Name:', font='Time_New_Roman 15')
        self.user_name_window = self.bg_canvas.create_window(30, 100, anchor='sw', window=self.user_name,
                                                             tags="Login_Text")

        self.user_name_entry = tk.Entry(self, font='Time_New_Roman 20')
        self.bg_canvas.create_window(150, 100, anchor='sw', window=self.user_name_entry,
                                     tags="Login Button")

        self.start_button = tk.Button(self, text="Start", font="Time_New_Roman 20", command=self.createIntroScreen2)
        self.start_button_window = self.bg_canvas.create_window(30, 200, anchor='sw', window=self.start_button,
                                                                tags="Start_Button")

        self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 20", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 100, self.height - 100,
                                                               anchor='sw', window=self.exit_button)
    
    def createIntroScreen2(self):
        self.name = "Default"
        if self.user_name_entry.get():
            self.name = self.user_name_entry.get()
            self.player.changeName(self.name)

        self.bg_canvas.destroy()
        self.original_image = Image.open('Images/bg.jpg').resize((self.screenWidth, self.screenHeight))
        self.bg = ImageTk.PhotoImage(self.original_image)

        # Make text printer object
        self.textPrinter = TextPrinter(self)

        self.bg_canvas = tk.Canvas(self, width=self.screenWidth, height=self.screenHeight)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')
        self.bg_canvas.create_text(self.width/2, self.height-600, font="Time_New_Roman 22", width=self.width, fill="white",
                                   text="You are a newly recruited Space Janitor sent"
                                   " out to salvage the numerous asteroids and ship wrecks that pollute space."
                                        f"\n\n Welcome, {self.name} to being a Space Janitor."
                                        "\nRise to the top.", tags="intro")
        self.next_text = tk.Button(self, font=5, text="Click here to Continue", command=self.createIntroScreen3)
        self.bg_canvas.create_window(self.width/2, self.height-100, anchor='center', window=self.next_text)

    def createIntroScreen3(self):
        self.bg_canvas.delete("intro")
        self.next_text.config(width=50, text="Start Game", command=self.createMainGUI)
        self.bg_canvas.create_text(self.width / 2 - 100, self.height - 500, font="Time_New_Roman 22", fill="white", justify="center",
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

    def createMainGUI(self):
         # Clear previous window
        self.bg_canvas.destroy()

        # Create Map Background
        self.background_image = Image.open('Images/HallWay.png').resize((self.screenWidth, self.screenHeight))
        self.backg = ImageTk.PhotoImage(self.background_image)


        self.original_image = Image.open('Map/Set/Main.jpg').resize((300, 400))
        self.bg = ImageTk.PhotoImage(self.original_image)


        # Create Menu Background
        menu_image = Image.open('Images/info_bg.png').resize((300, 300))
        self.menu_bg = ImageTk.PhotoImage(menu_image)


        self.bg_canvas = tk.Canvas(self, width=self.screenWidth, height=self.screenHeight)
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.backg, anchor='nw')
      
        # Create Canvas and Images
        self.bg_canvas.create_image(self.screenWidth - 1280 , self.screenWidth - 1280, image=self.bg, anchor='nw')
        self.bg_canvas.create_image(self.screenWidth - 1280 , (self.screenHeight / 2) + 130, image=self.menu_bg, anchor='nw')    


        self.start_game()

    def start_game(self):
         # Character Detail Button
        char_screen_button = tk.Button(self, font=5, height=2, text="Character\nDetails",
                                       command=lambda: self.openCharacterGUI())
        self.bg_canvas.create_window(self.screenWidth - 1260, self.screenHeight - 400,
                                     anchor='nw',window=char_screen_button, tags="Char_Screen")

        # Inventory Detail Button
        inv_screen_button = tk.Button(self, font=5, height=2, text="Inventory\nDetails",
                                      command=lambda: self.openInventoryGUI())
        self.bg_canvas.create_window(self.screenWidth - 1100, self.screenHeight - 400,
                                     anchor='nw',window=inv_screen_button, tags="Inv_Screen")

        # Test FightGUI - Delete once usable
        # fight_room = Dungeon("Fight Room", "None")
        # fight_room.type = "combat"
        # fight_room.generate(self.player.stats["Level"])
        # fight_button = tk.Button(self, font=5, height=3, text="Test Combat Screen",
        #                          command=lambda: FightGUI(fight_room, self.player))
        # self.bg_canvas.create_window(400, 475, anchor='nw', window=fight_button, tags="fight")

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 20", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.screenWidth - 90, self.screenHeight - 20, anchor='sw',window=self.exit_button)
        
        self.bg_canvas.create_text(450, 350, width=500, font=('Time_New_Roman', 15), fill="#FFFFFF", justify="left", anchor="w",
                                text="\nYou are ready to start cleaning up the wreckage."
                                    " Which wreckage should you visit first?"
                                    " Choose a location on the map.\n", tags="game_text")
        
        self.map = self.gameHandler.getMap()
        self.map.getCurrentRoom().clearRoom(True)
        # self.map.printMap()
        # self.display_image_buttons()

        self.bg_canvas.create_rectangle(800,800,900,900,fill="#0865A0")

        self.display_buttons()

        
    def display_buttons(self):
        # Remove previous buttons
        self.bg_canvas.delete("button")
        offset = 30
        
        self.button_frame = tk.Frame(self.bg_canvas, bg='#0865A0', relief=tk.SUNKEN, borderwidth=3)
        self.button_frame.place(relwidth=0.20, relheight=0.4, relx=0.78, rely=0.5)

        # for adjacentRoom in self.map.getCurrentRoom().getAdjacentRooms():
        #     callback = lambda room: lambda : self.handleButtonInput(room)
        #     button = tk.Button(self, font=5, height=1, text=(adjacentRoom.name), command=callback(adjacentRoom))
        #     self.bg_canvas.create_window(50, offset, anchor='nw',window=button,tags="button")
        #     offset += 50
        
        for adjacentRoom in self.map.getCurrentRoom().getAdjacentRooms():
            test = lambda room: lambda : self.handleButtonInput(room)
            button_text = adjacentRoom.name  # Button text

            # Create a button with a lambda function to pass the button_text as an argument
            button = tk.Button(self.button_frame, font=5, height=1, text=button_text, command=test(adjacentRoom), )
            button.pack(pady=5)
            offset += 50
            
    def handleButtonInput(self, room):
        self.gameHandler.enterRoom(room)
        self.clicked_button(room.name)


    def clicked_button(self, button_name):
        # list of current Rooms
        button_name = button_name.strip()
        button_images = [ "Weapons Bay", "Main Cabin", "Elevator 1", "Storage Area", "Kitchen", "Barracks", "Cafeteria",
            "Life Pod 1", "Cabin 2", "Showers", "Cabin 1", "Docking Port", "Bridge", "Elevator 3", "Elevator 2", "Cabin 3",
            "Captains Cabin", "Hangar", "Life Pod 2", "Engine Room"]

        if button_name in button_images:
            self.original_image = Image.open('Map/Set/'+ button_name + '.jpg').resize((300, 400))
            self.bg = ImageTk.PhotoImage(self.original_image)
            self.bg_canvas.create_image(self.screenWidth - 1280 , self.screenWidth - 1280, image=self.bg, anchor='nw')
        else: 
            print(f"did not find image at 'Map/Set/{button_name}.jpg'")



    def animate_text(self, text_id, text):
        self.textPrinter.animate_text(text, text_id, tk.END)

    def enterRepeatedRoom(self, room):
            self.textPrinter.animate_text(f"\n{room} has already been entered.", "game_text", tk.END)

    def enterChestRoom(self, room):
        self.textPrinter.animate_text(f"\nYou have entered {room} which contains a chest.\n",
                                      "game_text", tk.END)
        self.map = self.gameHandler.getMap()
        # self.map.printMap()
        self.display_buttons()
        # print(self.map.getCurrentRoom().getAdjacentRooms())

    def enterShopRoom(self, room):
        self.textPrinter.animate_text(f"\nYou have entered {room} which contains a shop.\n",
                                      "game_text", tk.END)
        self.map = self.gameHandler.getMap()
        # self.map.printMap()
        self.display_buttons()
        self.ready = True
        # print(self.map.getCurrentRoom().getAdjacentRooms())

    def enterCombatRoom(self, room):
        self.textPrinter.animate_text(f"\nYou have entered {room} which contains combat.\n",
                                      "game_text", tk.END)
        self.map = self.gameHandler.getMap()
        # self.map.printMap()
        self.display_buttons()
        # print(self.map.getCurrentRoom().getAdjacentRooms())


    def enterBossRoom(self, room):
        self.textPrinter.animate_text(f"\n You have entered {room} which is the boss room", "game_text", tk.END)

    def exitBossRoom(self, room):
        self.textPrinter.animate_text(f"\nCongratulations for beating the boss!", "game_text", tk.END)
        
    def exitRoom(self, room):
        self.textPrinter.animate_text(f"\nYou have exited {room}.", "game_text", tk.END)
    
    def exitCombatRoom(self, room):
        self.textPrinter.animate_text(f"\nYou have beaten the enemies in {room}", "game_text", tk.END)





    def openInventoryGUI(self):
        if self.ready and self.map.getCurrentRoom().getCleared():
            self.ready = False
            self.map.getCurrentRoom().clearRoom(False)
            self.InventoryGUI = InventoryGUI(self.player, self.map.getCurrentRoom(), self)

    def openCharacterGUI(self):
        if self.ready and self.map.getCurrentRoom().getCleared():
            self.ready = False
            self.map.getCurrentRoom().clearRoom(False)
            CharacterGUI(self.player, self.map.getCurrentRoom(), self)
