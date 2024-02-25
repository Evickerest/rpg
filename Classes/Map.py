import random
from Classes.Rooms.ChestRoom import ChestRoom
from Classes.Rooms.ShopRoom import ShopRoom
from Classes.Rooms.CombatRoom import CombatRoom
from Classes.Character import *

# Manages the rooms and room connections

class Map:
    def __init__(self):
        self.rooms = None
        self.currentRoom = None

        self.roomStats = {
            "Combat": {
                "desired_number": 5,
                "number_variance": 0.2,
                "room": CombatRoom
            },
            "Chest": {
                "desired_number": 1,
                "number_variance": 0.5,
                "room": ChestRoom
            },
            "Shop": {
                "desired_number": 1,
                "number_variance": 0.5,
                "room": ShopRoom
            }
        }

        self.generateMap()


    def generateMap(self):
        self.createRandomRooms()
        self.assignAdjacentRooms()
        self.setCurrentRoom(self.rooms[0])


    def getCurrentRoom(self):
        return self.currentRoom
    
    def setCurrentRoom(self, room):
        self.currentRoom = room

    def assignAdjacentRooms(self, percent=0.3):
        numberOfRooms = len(self.rooms)

        # For a visual representation of adjacent rooms
        # Will probably be used later to create a visual map
        arr = [[0]*numberOfRooms for i in range(numberOfRooms)]

        for i in range(numberOfRooms):
            currentRoom = self.rooms[i]
            # If a is connected to b, b is connected to a
            # We only need to loop through the connection one way
            for j in range(i, numberOfRooms):
                # Room Can't be connected to itself
                if j == i: continue
                # If true, then a connected be room i and j is made
                if random.random() <= percent:
                    adjacentRoom = self.rooms[j]
                    currentRoom.createAdjacency(adjacentRoom)
                    arr[i][j] = 1
            # In case no connections were made for a room
            if arr[i].count(1) == 0:
                randomColumn = random.randint(i,numberOfRooms-1)
                adjacentRoom = self.rooms[randomColumn]
                arr[i][randomColumn] = 1
                currentRoom.createAdjacency(adjacentRoom)    
        self.adjacencyMatrix = arr
        
    def createRandomRooms(self):
        rooms = []
        # For each key in the roomStats dictionary,
        # Create that set of rooms for only that room type
        for typeOfRoom in self.roomStats:
            counter = 0; 
            # Once we hit the desired number of rooms, it is up to luck if any more is created
            while (counter <= self.roomStats[typeOfRoom]["desired_number"] ) \
                    or random.random() <= self.roomStats[typeOfRoom]["number_variance"]:
                room = self.roomStats[typeOfRoom]["room"]()
                rooms.append( room )
                counter+=1
        random.shuffle(rooms)
        self.rooms = rooms

    def printMap(self):
        for row in self.adjacencyMatrix:
            print(f"{row}")
        for room in self.rooms:
            print(room,"\n")
