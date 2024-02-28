import csv
import random


class Room:
    def __init__(self):
        self.adjacentRooms = []
        self.isCurrentlyEntered = False
        self.hasEntered  = False
        self.cleared = False

    def enterRoom(self):
        pass

    def clearRoom(self, status: bool):
        self.cleared = status

    def getCleared(self):
        return self.cleared

    def createAdjacency(self, otherRoom):
        self.adjacentRooms.append(otherRoom)
        otherRoom.addAdjacentRoom(self)

    def addAdjacentRoom(self, otherRoom):
        self.adjacentRooms.append(otherRoom)

    def getAdjacentRooms(self):
        return self.adjacentRooms
    
    def generateName(self, roomType):
        names = []
        with open(f'Names/{roomType}RoomNames.txt', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                names.append(row)
        return random.choice(*names)
    
    def __repr__(self):
        return self.name
    



    # def generate_special(self, type: str, player: Player):
    #     if type == "combat":
    #         self.generate(player.stats["Level"])
    #     elif type == "rest":
    #         player.updateMaxHealth()
    #         player.updateHealth(player.stats["Max Health"])
    #     elif type == "shop":
    #         self.items.append(Item(random.choice(Item.ITEMS)))
    #     elif type == "chest":
    #         self.items.append(Item(random.choice(Item.ITEMS)))
        
         # def generatePossibleRooms(self):
    #     rooms = []
    #     with open('Names/room_txt/room_names', 'r') as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             rooms.append(row)
    #     return rooms