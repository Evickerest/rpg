
"""Module containing the ShopGUI class.
"""


import tkinter as tk
from PIL import ImageTk, Image
from Classes.character import Player
from Classes.Rooms.shop_room import ShopRoom


class ShopGUI(tk.Toplevel):
    """Class governing player actions while the Player instance is in
     a ShopRoom.
    """
    def __init__(self, room: ShopRoom, player: Player, gameHandler):
        """Method to equip an item from the Player's inventory.
        Args:
            room (ShopRoom): The ShopRoom instance to interact with
            player (Player): The Player instance to interact with.
            gameHandler: The game_handler instance.
        """
    

        super().__init__()
        self.title("Shop Inventory")
        self.geometry(f'{1100}x{700}+400+50')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.minsize(self.width, self.height)  # Min size, can be maximized.
        self.iconbitmap('Images/LevelOne/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.player = player
        self.shop = room
        self.game_handler = gameHandler
        self.item_entry = None
        self.inventory_text = ""
        self.shop_text = ""

        self.original_image = Image.open('Images/LevelOne/ShopStore.jpg').resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height,
                                   bg="black")
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        self.exit_button = tk.Button(self, text="Close",
                                     font="Cambria_Math 8 bold",
                                     command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 100, 50,
                                                               anchor='sw',
                                                               window=self.exit_button)

        self.bg_canvas.create_text(self.width / 2 - 350, self.height - 580,
                                   font='Cambria_Math 13 bold', fill="#FFFFFF", justify="left",
                                   text=self.player.name + "'s Equipment",
                                   tags="equipment_title")
        self.bg_canvas.create_text(self.width / 2 + 20, self.height - 580,
                                   font='Cambria_Math 13 bold', fill="#FFFFFF", justify="left",
                                   text=self.player.name + "'s Inventory",
                                   tags="inventory_title")
        self.bg_canvas.create_text(self.width / 2 + 270, self.height - 580,
                                   font='Cambria_Math 13 bold', fill="#FFFFFF", justify="left",
                                   text=self.shop.name + "'s Shop",
                                   tags="shop_title")

        self.unequip_button = tk.Button(self, text='Unequip Entered Item'
                                                   '\nFrom Equipment',
                                        font='Cambria_Math 8 bold',
                                        command=lambda: self.remove_equipped_item())
        self.unequip_button_window = self.bg_canvas.create_window(50, 500,
                                                                  anchor='sw',
                                                                  window=self.unequip_button,
                                                                  tags="unequip_button")

        self.equip_button = tk.Button(self, text='Equip Entered Item'
                                                 '\nFrom Inventory',
                                      font='Cambria_Math 8 bold',
                                      command=lambda: self.equip_item_inventory())
        self.equip_button_window = self.bg_canvas.create_window(250, 500,
                                                                anchor='sw',
                                                                window=self.equip_button,
                                                                tags="equip_button")

        self.purchase_button = tk.Button(self, text='Purchase Entered Item'
                                                    '\nFrom Shop',
                                         font='Cambria_Math 8 bold',
                                         command=lambda: self.buy_item_from_shop())
        self.purchase_button_window = self.bg_canvas.create_window(450, 500,
                                                                   anchor='sw',
                                                                   window=self.purchase_button,
                                                                   tags="buy_button")

        self.sell_button = tk.Button(self, text='Sell Entered Item'
                                                '\nFrom Inventory',
                                     font='Cambria_Math 8 bold',
                                     command=lambda: self.sell_item_inventory())
        self.sell_button_window = self.bg_canvas.create_window(650, 500,
                                                               anchor='sw',
                                                               window=self.sell_button,
                                                               tags="sell_button")

        self.buy_medkit_button = tk.Button(self, text='Buy Medkit\n'
                                                      'For 3 Credits',
                                           font='Cambria_Math 8 bold',
                                           command=lambda: self.buy_medkits())
        self.buy_medkit_button_window = self.bg_canvas.create_window(850, 500,
                                                                     anchor='sw',
                                                                     window=self.buy_medkit_button,
                                                                     tags="medkit_button")

        self.item_entry_text = tk.Label(self, text='Enter Item Below To Start',
                                        font='Cambria_Math 8 bold')
        self.item_entry_text = self.bg_canvas.create_window(self.width / 2 - 100, 550,
                                                            anchor='sw',
                                                            window=self.item_entry_text,
                                                            tags="item_entry_text")
        self.item_entry_box = tk.Entry(self, font='Cambria_Math 8 bold')
        self.bg_canvas.create_window(self.width / 2 - 100, 580, anchor='sw',
                                     window=self.item_entry_box,
                                     tags="item_entry")

        self.update_shop_gui()
        self.mainloop()

    def equipment_grid(self):
        """Creates and updates the Player instance's equipment display.
        """
        self.bg_canvas.delete("equipment")
        if self.player.equipment:
            self.bg_canvas.create_text(self.width / 2 - 300, self.height - 450,
                                       font="Cambria_Math 13 bold",
                                       fill="#FFFFFF", justify="left",
                                       text="\nHead Armor:\t"
                                       + str(self.player.equipment["Head"].stats["name"]) + ":\t+"
                                       + str(self.player.equipment["Head"].stats["defense"])
                                       + " Defense" + "\nArm Armor:\t"
                                       + str(self.player.equipment["Arms"].stats["name"]) + ":\t+"
                                       + str(self.player.equipment["Arms"].stats["defense"])
                                       + " Defense" + "\nChest Armor:\t"
                                       + str(self.player.equipment["Chest"].stats["name"]) + ":\t+"
                                       + str(self.player.equipment["Chest"].stats["defense"])
                                       + " Defense" + "\nLeg Armor:\t"
                                       + str(self.player.equipment["Legs"].stats["name"]) + ":\t+"
                                       + str(self.player.equipment["Legs"].stats["defense"])
                                       + " Defense" + "\nFoot Armor:\t"
                                       + str(self.player.equipment["Feet"].stats["name"]) + ":\t+"
                                       + str(self.player.equipment["Feet"].stats["defense"])
                                       + " Defense" + "\nWeapon:\t\t"
                                       + str(self.player.equipment["Weapon"].stats["name"]) + ":\t+"
                                       + str(self.player.equipment["Weapon"].stats["damage"])
                                       + " Damage" + "\n\nTotal Attack:\t"
                                       + str(self.player.get_attack()) +
                                       "\nTotal Defense:\t"
                                       + str(self.player.get_defense())
                                       + "\nMedkits:\t"
                                       + str(self.player.med_kits)
                                       + "\nCredits:\t"
                                       + str(self.player.stats["Credits"]),
                                       tags="equipment")

    def inventory_grid(self):
        """Creates and updates the Player instance's inventory display.
        """
        self.bg_canvas.delete("inventory")
        self.inventory_text = ""
        if len(self.player.inventory) > 0:
            for item in self.player.inventory:
                if item.stats["type"] == "Weapon":
                    self.inventory_text += ("\n\n" + str(item.stats["name"]) +
                                            ": +" + str(item.stats["damage"])
                                            + " Damage" + "\nValue: "
                                            + str(item.stats["value"]))
                else:
                    self.inventory_text += ("\n\n" + str(item.stats["name"]) +
                                            ": +" + str(item.stats["defense"])
                                            + " Defense" + "\nValue: " +
                                            str(item.stats["value"]))
        else:
            self.inventory_text = "Your Inventory\nIs Empty"
        self.bg_canvas.create_text(self.width / 2 + 20, self.height - 450,
                                   font='Cambria_Math 13 bold', fill="#FFFFFF", justify="left",
                                   text=self.inventory_text, tags="inventory")

    def shop_grid(self):
        """Creates and updates the ShopRoom instance's items.
        """
        self.bg_canvas.delete("shop")
        self.shop_text = ""
        if len(self.shop.items) > 0:
            for item in self.shop.items:
                if item.stats["type"] == "Weapon":
                    self.shop_text += ("\n" + str(item.stats["name"]) + ": +"
                                       + str(item.stats["damage"]) + " Damage"
                                       + "\nValue: "
                                       + str(item.stats["value"]))
                else:
                    self.shop_text += ("\n" + str(item.stats["name"]) + ": +"
                                       + str(item.stats["defense"])
                                       + " Defense" + "\nValue: " +
                                       str(item.stats["value"]))
        else:
            self.shop_text = "The Shop Is Empty"
        self.bg_canvas.create_text(self.width / 2 + 270, self.height - 450,
                                   font='Cambria_Math 13 bold', fill="#FFFFFF", justify="left",
                                   text=self.shop_text, tags="shop")

    def update_shop_gui(self):
        """Calls on and updates the entire display..
        """
        self.equipment_grid()
        self.inventory_grid()
        self.shop_grid()

    def equip_item_inventory(self):
        """Method to read input from an entry_box and equip the specified Item.
        """
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_equip = self.item_entry
            for item in self.player.inventory:
                if item.stats["name"] == item_to_equip:
                    self.player.equip_item(item)
                    self.player.update_defense()
                    self.player.update_attack()
                    self.update_shop_gui()

    def remove_equipped_item(self):
        """Method to read input from an entry_box and unequip the
         specified Item.
        """
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_remove = self.item_entry
            for item in self.player.equipment.values():
                if item.stats["name"] == item_to_remove:
                    self.player.unequip_item(item)
                    self.player.update_defense()
                    self.player.update_attack()
                    self.update_shop_gui()

    def buy_item_from_shop(self):
        """Method to read input from an entry_box and buy the specified
         Item from the ShopRoom.
        """
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_buy = self.item_entry
            for item in self.shop.items:
                if item.stats["name"] == item_to_buy:
                    if self.player.stats["Credits"] >= item.stats["value"]:
                        self.player.add_item(item)
                        self.shop.items.remove(item)
                        self.player.stats["Credits"] -= item.stats["value"]
                        self.update_shop_gui()

    def sell_item_inventory(self):
        """Method to read input from an entry_box and sell the specified
         Item to the ShopRoom.
        """
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_sell = self.item_entry
            for item in self.player.inventory:
                if item.stats["name"] == item_to_sell:
                    self.player.drop_item(item)
                    self.player.stats["Credits"] += item.stats["value"]
                    self.shop.items.append(item)
                    self.update_shop_gui()

    def buy_medkits(self):
        """Method for the Player instance to buy Medkits in exchange
         for Credits.
        """
        if self.player.stats["Credits"] >= 3:
            self.player.med_kits = 1
            self.player.stats["Credits"] -= 3
            self.update_shop_gui()

    def read_entry_box(self) -> None | str:
        """Method to read input from an entry_box.
        Returns:
            item_entry: The string representation of the input.
             None if no input was detected.
        """
        self.item_entry = None
        if self.item_entry_box.get():
            self.item_entry = self.item_entry_box.get()
        return self.item_entry

    def destroy(self):
        """Method governing what happens when the instance is destroyed.
        """
        self.shop.clear_room(True)
        self.game_handler.exit_room(self.shop)
        super().destroy()
