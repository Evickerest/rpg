import csv
import random


class Room:
    def __init__(self):
        self.adjacentRooms = []
        self.isCurrentlyEntered = False
        self.hasEntered  = False
        self.cleared = False

        self.posX = None
        self.posY = None

    def setCoordinates(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def getCoordinates(self):
        return [self.posX,self.posY]

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
    
    def __eq__(self, other):
        return self.posX == other.posX and self.posY == other.posY
