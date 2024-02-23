import tkinter as tk
from Classes.Character import *
from Classes.Rooms.Room import *
from PIL import ImageTk, Image


class ShopGUI(tk.Toplevel):
    def __init__(self, room: Room, player: Player):
        super().__init__()
        self.title("Shop Inventory")
        self.geometry(f'{800}x{600}+170+250')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.minsize(self.width, self.height)  # Minimum size of the window, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.player = player
        self.shop = room

        num_items = randint(1, 5)
        for i in range(1, num_items):
            self.shop.generate_special(self.shop.type, self.player)

        self.original_image = Image.open('Images/bg2.jpeg').resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height, bg="black")
        self.bg_canvas.pack(fill='both', expand=True)

        self.exit_button = tk.Button(self, text="Close", font="Time_New_Roman 8", command=self.destroy)
        self.exit_button_window = self.bg_canvas.create_window(self.width - 60, 580,
                                                               anchor='sw', window=self.exit_button)

        self.bg_canvas.create_text(self.width / 2 - 250, self.height - 580, font=8, fill="blue", justify="center",
                                   text=self.player.name + "'s Equipment", tags="equipment_title")
        self.bg_canvas.create_text(self.width / 2 + 70, self.height - 580, font=8, fill="blue", justify="center",
                                   text=self.player.name + "'s Inventory", tags="inventory_title")
        self.bg_canvas.create_text(self.width / 2 + 320, self.height - 580, font=8, fill="blue", justify="center",
                                   text=self.shop.name + "'s Shop", tags="shop_title")

        self.unequip_button = tk.Button(self, text='Unequip Entered Item\nFrom Equipment',
                                        font='Time_New_Roman 8', command=lambda: self.removeEquippedItem())
        self.unequip_button_window = self.bg_canvas.create_window(50, 400, anchor='sw',
                                                                  window=self.unequip_button, tags="unequip_button")

        self.equip_button = tk.Button(self, text='Equip Entered Item\nFrom Inventory',
                                      font='Time_New_Roman 8', command=lambda: self.equipItemInventory())
        self.equip_button_window = self.bg_canvas.create_window(250, 400, anchor='sw',
                                                                window=self.equip_button, tags="equip_button")

        self.purchase_button = tk.Button(self, text='Purchase Entered Item\nFrom Shop',
                                         font='Time_New_Roman 8', command=lambda: self.BuyItemFromShop())
        self.purchase_button_window = self.bg_canvas.create_window(450, 400, anchor='sw',
                                                                   window=self.purchase_button, tags="buy_button")

        self.sell_button = tk.Button(self, text='Sell Entered Item\nFrom Inventory',
                                     font='Time_New_Roman 8', command=lambda: self.sellItemInventory())
        self.sell_button_window = self.bg_canvas.create_window(650, 400, anchor='sw',
                                                               window=self.sell_button, tags="sell_button")

        self.item_entry_text = tk.Label(self, text='Enter Item Below To Start', font='Time_New_Roman 10')
        self.item_entry_text = self.bg_canvas.create_window(self.width / 2 - 100, 450, anchor='sw',
                                                            window=self.item_entry_text, tags="item_entry_text")
        self.item_entry_box = tk.Entry(self, font='Time_New_Roman 8')
        self.bg_canvas.create_window(self.width / 2 - 100, 480, anchor='sw',
                                     window=self.item_entry_box, tags="item_entry")

        self.updateShopGui()
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
        self.bg_canvas.create_text(self.width / 2 + 70, self.height - 450, font=8, fill="blue", justify="center",
                                   text=self.inventory_text, tags="inventory")

    def shop_grid(self):
        self.bg_canvas.delete("shop")
        self.shop_text = ""
        if len(self.shop.items) > 0:
            for item in self.shop.items:
                if item.stats["type"] == "Weapon":
                    self.shop_text += ("\n\n" + str(item.stats["name"]) + ": +"
                                       + str(item.stats["damage"]) + " Damage")
                else:
                    self.shop_text += ("\n\n" + str(item.stats["name"]) + ": +"
                                       + str(item.stats["defense"]) + " Defense")
        else:
            self.shop_text = "The Shop Is Empty"
        self.bg_canvas.create_text(self.width / 2 + 320, self.height - 450, font=8, fill="blue", justify="center",
                                   text=self.shop_text, tags="shop")

    def updateShopGui(self):
        self.equipment_grid()
        self.inventory_grid()
        self.shop_grid()
        self.bg_canvas.create_text(self.width / 2 - 250, self.height - 270, font=8, fill="blue", justify="center",
                                   text="Credits: " + str(self.player.stats["Credits"]), tags="credits")

    def equipItemInventory(self):
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_equip = self.item_entry
            for item in self.player.inventory:
                if item.stats["name"] == item_to_equip:
                    self.player.equipItem(item)
                    self.updateShopGui()

    def removeEquippedItem(self):
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_remove = self.item_entry
            for item in self.player.equipment.values():
                if item.stats["name"] == item_to_remove:
                    self.player.unequipItem(item)
                    self.updateShopGui()

    def BuyItemFromShop(self):
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_buy = self.item_entry
            for item in self.shop.items:
                if item.stats["name"] == item_to_buy:
                    if self.player.stats["Credits"] >= item.stats["value"]:
                        self.player.addItem(item)
                        self.shop.items.remove(item)
                        self.updateShopGui()

    def sellItemInventory(self):
        self.read_entry_box()
        if self.read_entry_box() is not None:
            item_to_sell = self.item_entry
            for item in self.player.inventory:
                if item.stats["name"] == item_to_sell:
                    self.player.dropItem(item)
                    self.player.stats["Credits"] += item.stats["value"]
                    self.shop.items.append(item)
                    self.updateShopGui()

    def read_entry_box(self) -> None | str:
        self.item_entry = None
        if self.item_entry_box.get():
            self.item_entry = self.item_entry_box.get()
        return self.item_entry
