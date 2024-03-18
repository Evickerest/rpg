"""Module containing the FightGUI class.
"""


import random
import tkinter as tk
from PIL import ImageTk, Image
from Classes.character import Player, Enemy, Character
from Classes.Rooms.combat_room import CombatRoom


class FightGUI(tk.Toplevel):
    """Class governing player-system interactions during an active FightRoom.
    """
    def __init__(self, room: CombatRoom, player: Player, game_handler):
        """Creates the instance.
        Args:
            room (CombatRoom): The CombatRoom instance.
            player (Player): The Player instance being controlled.
            game_handler: The gameHandler instance.
        """

        super().__init__()
        self.title("Combat Screen")
        self.geometry(f'{800}x{600}+400+50')
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.minsize(self.width, self.height)  # Min size, can be maximized.
        self.iconbitmap('Images/SpaceShip.ico')
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.player = player
        self.room = room
        self.enemies = room.enemies
        self.room_name = room.__repr__()
        self.game_handler = game_handler
        self.no_enemy = False
        self.enemies_txt = ""
        self.count = 0
        self.enemy_entry = None
        self.exit_button = None
        self.exit_button_window = None
        self.turn_counter = 0
        self.player_txt1 = ""
        self.player_txt2 = ""
        self.enemy_txt1 = ""
        self.enemy_txt2 = ""


        self.original_image = Image.open('Images/' + self.room_name + '.jpg').resize((self.width,
                                                                                      self.height))
        self.bg = ImageTk.PhotoImage(self.original_image)

        self.bg_canvas = tk.Canvas(self, width=self.width, height=self.height,
                                   bg="#043F5B")
        self.bg_canvas.pack(fill='both', expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        self.bg_canvas.create_text(self.width / 2 - 250, self.height - 580,
                                   font="Cambria_Math 14 bold", fill="white", justify="center",
                                   text=self.player.name + "'s Side",
                                   tags="equipment_title")

        t = "Enemies' Side" if not self.room.is_boss_room else "Boss Side"
        self.bg_canvas.create_text(self.width / 2 + 250, self.height - 580,
                                   font="Cambria_Math 14 bold", fill="white", justify="center",
                                   text=t, tags="Enemies")

        self.enemy_entry_text = tk.Label(self, text='Enemy # To Attack',
                                         font="Cambria_Math 9 bold")
        self.enemy_entry_text = self.bg_canvas.create_window(50, 430,
                                                             anchor='sw',
                                                             window=self.enemy_entry_text,
                                                             tags="enemy_entry_text")
        self.enemy_entry_box = tk.Entry(self, font="Cambria_Math 9 bold")
        self.bg_canvas.create_window(50, 450, anchor='sw',
                                     window=self.enemy_entry_box,
                                     tags="enemy_entry")

        self.attack_button = tk.Button(self, text='Attack',
                                       font="Cambria_Math 9 bold",
                                       command=lambda: self.player_attack())
        self.attack_button_window = self.bg_canvas.create_window(50, 400,
                                                                 anchor='sw',
                                                                 window=self.attack_button,
                                                                 tags="attack_button")

        self.defend_button = tk.Button(self, text='Defend',
                                       font="Cambria_Math 9 bold",
                                       command=lambda: self.defend(self.player))
        self.defend_button_window = self.bg_canvas.create_window(250, 400,
                                                                 anchor='sw',
                                                                 window=self.defend_button,
                                                                 tags="defend_button")

        self.use_medkit_button = tk.Button(self, text='Use Medkit',
                                           font="Cambria_Math 9 bold",
                                           command=lambda: self.use_medkit())
        self.use_medkit_button_window = self.bg_canvas.create_window(450, 400,
                                                                     anchor='sw',
                                                                     window=self.use_medkit_button,
                                                                     tags="medkit_button")

        self.combat_log()

        # self.use_item_button = tk.Button(self, text='Placeholder\n',
        #                                  font="Cambria_Math 14 bold",
        #                                  command=lambda: self.destroy())
        # self.use_item_button_window = self.bg_canvas.create_window(650, 400,
        #                                                            anchor='sw',
        #                                                            window=self.use_item_button,
        #                                                            tags="use_item_button")

        self.update_combat_gui()
        self.mainloop()

    def player_grid(self):
        """Creates and updates the player's side of the display.
        """
        self.bg_canvas.delete("health", "attack", "defense", "medkits")
        self.bg_canvas.create_text(50, self.height - 300, anchor='sw', font="Cambria_Math 14 bold",
                                   fill="white", justify="center",
                                   text="Health:\t"
                                   + str(self.player.stats["Health"]) + " / "
                                   + str(self.player.stats["Max Health"]),
                                   tags="health")
        self.bg_canvas.create_text(50, self.height - 270, anchor='sw', font="Cambria_Math 14 bold",
                                   fill="white", justify="center",
                                   text="Attack:\t" + str(self.player.attack),
                                   tags="ff0d1d")
        self.bg_canvas.create_text(50, self.height - 240, anchor='sw', font="Cambria_Math 14 bold",
                                   fill="white", justify="center",
                                   text="Defense:\t" + str(self.player.defense),
                                   tags="defense")
        self.bg_canvas.create_text(self.width / 2 + 50, self.height - 240,
                                   anchor='sw', font="Cambria_Math 14 bold", fill="white",
                                   justify="center", tags="medkits",
                                   text="Medkits: "
                                        + str(self.player.stats["Medkits"]))

    def update_combat_gui(self):
        """Calls all parts of the GUI display and updates it.
        """
        self.player_grid()
        self.enemy_grid()
        self.make_exit()

    def enemy_grid(self):
        """Creates and updates the display for all enemies.
        """
        self.bg_canvas.delete("enemies")
        self.enemies_txt = ""
        self.count = 0
        if len(self.enemies) > 0:
            for enemy in self.enemies:
                self.enemies_txt += ("\n" + str(self.count) + ") "
                                     + str(enemy.name) + "\n  "
                                     + "LV: " + str(enemy.stats["Level"])
                                     + " | Health: "
                                     + str(enemy.stats["Health"]) + "\n  "
                                     + str(enemy.get_attack()) + " Damage | "
                                     + str(enemy.get_defense()) + " Defense")
                self.count += 1
        else:
            self.enemies_txt = "No Enemies Remain"
        self.bg_canvas.create_text(self.width / 2 + 250, self.height - 430,
                                   font="Cambria_Math 14 bold", fill="white", justify="center",
                                   text=self.enemies_txt, tags="enemies")

    def read_entry_box(self) -> None | str:
        """Reads the input from the enemy_entry_box.
        Returns:
            None: No input in the enemy_entry_box.
            str: The string representation of the input.
        """
        self.enemy_entry = None
        if self.enemy_entry_box.get():
            self.enemy_entry = self.enemy_entry_box.get()
        return self.enemy_entry

    # def enemy_attack(self, attacker: Character, target: Player):
    #     """Method governing how an Enemy instance attacks the Player instance.
    #     Args:
    #         attacker (Character): The Character instance doing the attack.
    #         target (Player): The Player instance being attacked.
    #     """
    #     if target.living:
    #         dead = target.take_damage(attacker)
    #         if dead:
    #             self.player.set_living(False)
    #             self.character_dead_gui()

    #     # For some reason not working
    #     if target.stats["Health"] < 1:
    #         self.player.set_living(False)
    #         attacker.stats["XP"] += target.stats["Level"] * 10

    #         self.character_dead_gui()

    #     if isinstance(attacker, Player):
    #         self.resolve_player_turn()

    #     if self.player.living:
    #         self.update_combat_gui()

    def player_attack(self):
        """Method governing how a Player attacks a target specified using
         the enemy_entry_box.
        """
        self.player_txt1 = ""
        if not self.player.living:
            return
        to_target = self.read_entry_box()
        if to_target is not None:
            if to_target.isnumeric():
                if int(to_target) < len(self.enemies):
                    target = self.enemies[int(to_target)]
                    damage = target.take_damage(self.player)
                    self.player_txt1 += (f"You hit {target.name} for {damage}"
                                         f" damage.\n")
                    if target.stats["Health"] < 1:
                        self.enemies.remove(target)
                        self.room.enemies_killed += 1
                        target.set_living(False)
                        self.enemy_entry_box.delete(0, 100)
                        self.player_txt1 += f"You killed {target.name}."
                        self.player.stats["XP"] += int(target.stats["Level"]
                                                       * 2.5)
                        self.player.stats["Credits"] += target.stats["Level"]
                    self.player_txt2 = self.player_txt1
                    self.resolve_player_turn()
        else:
            pass
        if self.player.living:
            self.update_combat_gui()

    def defend(self, defender: Character):
        """Method to temporarily increase a Character's defense
        Args:
            defender (Character): The Character instance that is defending.
        """
        defender.defend_action()
        if isinstance(defender, Player):
            self.player_txt1 = ""
            self.player_txt1 += (f"You are defending.\nYour defense is"
                                 f" temporarily increased to"
                                 f" {self.player.defense}.")
            self.player_txt2 = self.player_txt1
            self.resolve_player_turn()
        if self.player.living:
            self.update_combat_gui()

    def use_medkit(self):
        """Method to use a medkit and update the display.
        """
        heal = self.player.use_medkits()
        self.player_txt1 = ""
        self.player_txt1 = f"You used a medkit and healed for {heal} health."
        self.player_txt2 = self.player_txt1
        self.resolve_player_turn()
        self.update_combat_gui()

    def resolve_player_turn(self):
        """Method to resolve enemy actions after the player's turn is over.
        """
        if self.player:
            self.enemy_txt1 = ""
            for enemy in self.enemies:
                enemy.update_defense()
                if self.player.living:
                    self.enemy_turn(enemy)
            self.player.update_defense()
            self.enemy_txt2 = self.enemy_txt1
            self.combat_log()
            self.turn_count()

    def enemy_turn(self, enemy: Enemy):
        """Method to randomly determine what an Enemy instance does.
        Args:
            enemy (Enemy): The Enemy instance doing the action.
        """
        choice = random.choice(["attack", "defend", "nothing"])
        if choice == "attack":
            damage = self.player.take_damage(enemy)
            self.enemy_txt1 += (f"{self.enemies.index(enemy)}) {enemy.name}"
                                f" attacked {self.player.name} for {damage}"
                                f" damage.\n")
            if self.player.stats["Health"] < 1:
                self.player.set_living(False)
                self.enemy_txt1 += "You were killed!\n"
                self.character_dead_gui()
        elif choice == "defend":
            self.defend(enemy)
            self.enemy_txt1 += (f"{self.enemies.index(enemy)}) {enemy.name} is defending. Their defense is"
                                f" temporarily {enemy.defense} now.\n")
        else:
            self.enemy_txt1 += f"{self.enemies.index(enemy)}) {enemy.name} did nothing.\n"


    def turn_count(self):
        """Increments turn_counter by 1.
        Returns:
            turn_counter (int): The current turn.
        """
        self.turn_counter += 1
        return self.turn_counter

    def combat_log(self):
        """Updates the combat log.
        """
        self.bg_canvas.delete("player_txt1", "player_txt2", "enemy_txt1", "enemy_txt2")
        self.bg_canvas.create_text(50, 100, width=200,
                                   font=('Time_New_Roman', 10), fill="#FFFFFF",
                                   justify="left", anchor="w",
                                   text=f"Last Turn (Turn {self.turn_counter}):\n"
                                   f"{self.player_txt2}", tags="player_txt1")
        self.bg_canvas.create_text(50, 250, width=200,
                                   font=('Time_New_Roman', 10), fill="#FFFFFF",
                                   justify="left", anchor="w",
                                   text=f"This Turn (Turn {self.turn_counter + 1}):\n"
                                   f"{self.player_txt1}", tags="player_txt2")
        self.bg_canvas.create_text(250, 100, width=300,
                                   font=('Time_New_Roman', 10), fill="#FFFFFF",
                                   justify="left", anchor="w",
                                   text=f"Last Turn (Turn {self.turn_counter}):\n"
                                   f"{self.enemy_txt1}", tags="enemy_txt1")
        self.bg_canvas.create_text(250, 250, width=300,
                                   font=('Time_New_Roman', 10), fill="#FFFFFF",
                                   justify="left", anchor="w",
                                   text=f"This Turn (Turn {self.turn_counter + 1}):\n"
                                   f"{self.enemy_txt2}", tags="enemy_txt1")

    def make_exit(self):
        """Method to make an exit after the fight is won.
        """
        if not self.enemies:
            self.exit_button = tk.Button(self, text="Exit",
                                         font="Cambria_Math 9 bold",
                                         command=self.endFight)
            self.exit_button_window = self.bg_canvas.create_window(self.width / 2 - 60, 380,
                                                                   anchor='sw',
                                                                   window=self.exit_button)
            self.bg_canvas.delete("attack_button", "defend_button",
                                  "use_item_button", "enemy_entry",
                                  "enemy_entry_text")

    def character_dead_gui(self):
        """Display GUI if character dies during combat.
        """
        print("Character is dead")
        super().destroy()
        self.game_handler.end_game(False)

        # self.bg_canvas.delete("attack_button", "defend_button",
        #                       "use_item_button", "enemy_entry",
        #                       "enemy_entry_text")

    def endFight(self):
        """Method handling when the instance can he exited and what happens.
        """
        if not self.enemies or not self.player.living:
            self.game_handler.exit_room(self.room)
            self.room.clear_room(True)
            super().destroy()
