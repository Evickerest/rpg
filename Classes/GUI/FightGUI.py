import random
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
        self.enemies = room.enemies

        self.no_enemy = False

        self.original_image = Image.open('Images/bg2.jpeg').resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height, bg="#043F5B")
        self.bg_canvas.pack(fill='both', expand=True)

        self.bg_canvas.create_text(self.width / 2 - 250, self.height - 580, font=10, fill="#06153E", justify="center",
                                   text=self.player.name + "'s Side", tags="equipment_title")
        self.bg_canvas.create_text(self.width / 2 + 250, self.height - 580, font=10, fill="#06153E", justify="center",
                                   text="Enemies' Side", tags="Enemies")

        self.displacement = 0
        self.count = 1
        for enemy in self.enemies:
            self.attack_button = tk.Button(self, text=f'{self.count}: Attack {enemy.name}',
                                           font='Time_New_Roman 8', command=lambda: self.attack(self.player, enemy))
            self.attack_button_window = self.bg_canvas.create_window(50, 400 + self.displacement, anchor='sw',
                                                                     window=self.attack_button,
                                                                     tags=f"attack_{self.count}")
            self.displacement += 30
            self.count += 1

        self.defend_button = tk.Button(self, text='Defend',
                                       font='Time_New_Roman 8', command=lambda: self.defend(self.player))
        self.defend_button_window = self.bg_canvas.create_window(250, 400, anchor='sw',
                                                                 window=self.defend_button, tags="defend_button")

        self.use_medkit_button = tk.Button(self, text='Use Medkit',
                                           font='Time_New_Roman 8', command=lambda: self.use_medkit())
        self.use_medkit_button_window = self.bg_canvas.create_window(450, 400, anchor='sw',
                                                                     window=self.use_medkit_button,
                                                                     tags="medkit_button")

        self.use_item_button = tk.Button(self, text='Placeholder\n',
                                         font='Time_New_Roman 8', command=lambda: self.destroy())
        self.use_item_button_window = self.bg_canvas.create_window(650, 400, anchor='sw',
                                                                   window=self.use_item_button, tags="use_item_button")

        self.updateCombatGUI()
        self.mainloop()

    def player_grid(self):
        self.bg_canvas.delete("health", "attack", "defense", "medkits")
        self.bg_canvas.create_text(50, self.height - 300, anchor='sw', font=8,
                                   fill="#06153E", justify="center",
                                   text="Health: " + str(self.player.stats["Health"])
                                   + " / " + str(self.player.stats["Max Health"]), tags="health")
        self.bg_canvas.create_text(50, self.height - 270, anchor='sw', font=8, fill="#06153E", justify="center",
                                   text="Attack: " + str(self.player.attack), tags="attack")
        self.bg_canvas.create_text(50, self.height - 240, anchor='sw', font=8, fill="#06153E", justify="center",
                                   text="Defense: " + str(self.player.defense), tags="defense")
        self.bg_canvas.create_text(self.width / 2 + 50, self.height - 240, anchor='sw',
                                   font=8, fill="#06153E", justify="center", tags="medkits",
                                   text="Medkits: " + str(self.player.stats["Medkits"]))

    def updateCombatGUI(self):
        self.player_grid()
        self.enemy_grid()
        self.updateAttackButtons()
        self.make_exit()

    def enemy_grid(self):
        self.bg_canvas.delete("enemies")
        self.enemies_txt = ""
        if len(self.enemies) > 0:
            for enemy in self.enemies:
                self.enemies_txt += ("\n\n" + str(enemy.name) + ": +"
                                     + str(enemy.getAttack()) + " Damage"
                                     + str(enemy.getDefense()) + " Defense")
        else:
            self.enemies_txt = "No Enemies Remain"
        self.bg_canvas.create_text(self.width / 2 + 250, self.height - 450, font=10, fill="#06153E", justify="center",
                                   text=self.enemies_txt, tags="enemies")

    def updateAttackButtons(self):
        self.displacement = 0
        for num in range(1, self.count):
            self.bg_canvas.delete(f'attack_{num}')
        self.count = 1
        for enemy in self.enemies:
            self.attack_button = tk.Button(self, text=f'{self.count}: Attack {enemy.name}',
                                           font='Time_New_Roman 8', command=lambda: self.attack(self.player, enemy))
            self.attack_button_window = self.bg_canvas.create_window(50, 400 + self.displacement, anchor='sw',
                                                                     window=self.attack_button,
                                                                     tags=f"attack_{self.count}")
            self.displacement += 30
            self.count += 1

    def attack(self, attacker: Character, target: Character):
        target.take_damage(attacker)
        if target.stats["Health"] < 1:
            self.enemies.remove(target)
        if isinstance(attacker, Player):
            self.resolve_player_turn()
        self.updateCombatGUI()

    def defend(self, defender: Character):
        defender.defend_action()
        if isinstance(defender, Player):
            self.resolve_player_turn()
        self.updateCombatGUI()


    def use_medkit(self):
        self.player.use_medkits()
        self.resolve_player_turn()
        self.updateCombatGUI()

    def resolve_player_turn(self):
        if self.player:
            for enemy in self.enemies:
                enemy.updateDefense()
                self.enemy_turn(enemy)
            self.player.updateDefense()

    def enemy_turn(self, enemy: Enemy):
        choice = random.choice(["attack", "defend", "nothing"])
        if choice == "attack":
            self.player.take_damage(enemy)
        elif choice == "defend":
            self.defend(enemy)

    def make_exit(self):
        if not self.enemies:
            self.exit_button = tk.Button(self, text="Exit", font="Time_New_Roman 10", command=self.destroy)
            self.exit_button_window = self.bg_canvas.create_window(self.width / 2 - 60, 380,
                                                                   anchor='sw', window=self.exit_button)
