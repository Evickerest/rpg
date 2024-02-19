import tkinter as tk
from Classes.Character import *
from PIL import ImageTk, Image


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
