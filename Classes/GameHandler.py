import csv
import random
from Classes.GUI.MainGui import MainGUI
from Classes.Character import Character, Player
from Classes.Map import Map
from Classes.dungeon import Dungeon


class GameHandler:
    def __init__(self):
        self.player = Player("Default", {"Strength": 5, "Dexterity": 5, "Vitality": 5,
                             "Intelligence": 5, "Level": 1, "XP": 0, "Stat Points": 5, "Credits": 0})
        self.GUI = MainGUI(self.player, self)

    def generatePossibleRooms(self):
        rooms = []
        with open('Names/room_txt/room_names', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                rooms.append(row)
        return rooms

    def generateMap(self):
        # Generate 5 room types
        randomRoomTypes = []
        rooms = []
        for index in range(5):
            randomRoomTypes.append(random.choice(["combat", "rest", "shop", "chest", "empty"]))

        for index in range(5):
            roomType = randomRoomTypes[index]
            rooms.append(Dungeon(f"room{index+1}", "room"))
        rooms.append(Dungeon("room6", "boss"))

        # Creates a Matrix that determines connectivity
        adjacencyMatrix = [[0]*6 for i in range(6)]

        # Create Random room connections
        for index in range(6):
            for subindex in range(6):
                if subindex == index:
                    continue
                if random.random() <= 0.5:
                    adjacencyMatrix[index][subindex] = 1
            # In case no connections were made for a room
            if adjacencyMatrix[index].count(1) == 0:
                adjacencyMatrix[index][0] = random.randint(1,6)

        self.map = Map(
            {
                "room1": rooms[0],
                "room2": rooms[1],
                "room3": rooms[2],
                "room4": rooms[3],
                "room5": rooms[4],
                "room6": rooms[5],
            }
        )

        for index in range(6):
            currentRoom = rooms[index]
            for subindex in range(6):
                value = adjacencyMatrix[index][subindex]
                adjacentRoom = rooms[subindex]

                if value != 0:
                    currentRoom.addAdjacentRoom(adjacentRoom)

        return self.map
