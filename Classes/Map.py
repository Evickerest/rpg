import math
import random
from Classes.Rooms.ChestRoom import ChestRoom
from Classes.Rooms.ShopRoom import ShopRoom
from Classes.Rooms.CombatRoom import CombatRoom
from Classes.Character import *
from math import hypot

# Manages the rooms and room connections

class Map:
    def __init__(self):
        self.rooms = None
        self.currentRoom = None

        self.TotalRooms = 4

        # Completely Arbitrary
        self.mapHeight = 50
        self.mapWidth = 50

        self.roomTypes = {
            "Combat": {
                "desired_number": 2,
                "room": CombatRoom
            },
            "Chest": {
                "desired_number": 1,
                "room": ChestRoom
            },
            "Shop": {
                "desired_number": 1,
                "room": ShopRoom
            }
        }

        self.generateMap()

    def generateMap(self):
        self.generateRandomRooms()
        self.connectAllTheRoomsTogether()
        self.createRoomEdges()
        self.setCurrentRoom(self.rooms[0])
        self.printMap()

    def getCurrentRoom(self):
        return self.currentRoom
    
    def setCurrentRoom(self, room):
        self.currentRoom = room

    def generateRandomRooms(self):
        self.rooms = []

        # Loop through each room type
        for roomType in self.roomTypes:
            # Loop for the desired number of rooms
            for _ in range(self.roomTypes[roomType]["desired_number"]):
                randomX = random.randint(1, self.mapWidth)
                randomY = random.randint(1, self.mapHeight)

                # Create room and set coordinates
                room = self.roomTypes[roomType]["room"]()
                room.setCoordinates(randomX, randomY)

                self.rooms.append( room )

    # Create 2d Square Array
    def createMultiArray(self, width):
        return [ [0 for _ in range(width)] for _ in range(width)]

    # Create a matrix that contains that distance from each room to every other room
    def connectAllTheRoomsTogether(self):
        self.edgeMatrix = self.createMultiArray(self.TotalRooms)

        print( self.edgeMatrix)

        for i in range(self.TotalRooms):
            for j in range(self.TotalRooms):
                if not self.rooms[i] == self.rooms[j]:
                    dist = math.dist(self.rooms[i].getCoordinates(), self.rooms[j].getCoordinates())
                    self.edgeMatrix[i][j] = round(dist,4)

        print(self.edgeMatrix)

    def getClosestNode(self, edgeList):
        # Removes 0s from array and sorts in ascending order
        arr = [i for i in edgeList if i != 0]
        arr.sort()

        # return closest node
        smallestWeight = arr[0]
        return self.rooms[edgeList.index(smallestWeight)]
        

    # Looks at each edge and only keeps the closest room
    def createRoomEdges(self):
        for index, edgeList in enumerate(self.edgeMatrix):
            currentNode = self.rooms[index]
            closestNode = self.getClosestNode(edgeList)

            currentNode.createAdjacency(closestNode)

            



    def printMap(self):
        for room in self.rooms:
            print(f"{room} is adjacent to: {room.getAdjacentRooms()}")


        






    

   
