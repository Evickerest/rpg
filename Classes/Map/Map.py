import math
import random
from Classes.Character import *
from Classes.Map.Edge import Edge
from Classes.Map.MapConstants import MapConstants

# Manages the rooms and room connections


class Map:
    def __init__(self):
        self.rooms = None
        self.currentRoom = None
        self.edges = []

        self.generateMap()

    def generateMap(self):
        self.generateRandomRooms()
        self.connectEveryRoomTogether()
        self.primsAlgorithm()
        self.setCurrentRoom(MapConstants.START_ROOM)
        self.assignRandomImages()
        # self.printMap()

    def getCurrentRoom(self):
        return self.currentRoom
    
    def setCurrentRoom(self, room):
        self.currentRoom = room

    def generateRandomRooms(self):
        self.rooms = []

        counter = 1
        # Loop through each room type
        for roomType in MapConstants.ROOM_TYPES:
            # Loop for the desired number of rooms
            for _ in range(MapConstants.ROOM_TYPES[roomType]["desired_number"]):
                randomX = random.random()
                randomY = random.random()

                # Create room and set coordinates
                room = MapConstants.ROOM_TYPES[roomType]["room"]()
                # room.image = randomImage()

                # TODO: delete later
                room.number = str(counter)
                counter += 1

                room.setCoordinates(randomX, randomY)

                self.rooms.append( room )

    # Create an edge between all possible pairs of rooms
    def connectEveryRoomTogether(self):
        for room in self.rooms:
            for otherRoom in self.rooms:
                if room != otherRoom:
                    room.edges.append(Edge(room, otherRoom))


    # Implementation of Prim's Algorithm
    # Takes a graph of nodes (rooms) and edges, and constructs a minimum spanning tree
    # Downside is that a mst doesn't produce cycles, so additional edges will have to be added in              
    def primsAlgorithm(self):
        seenRooms = [self.rooms[0]]
        defaultEdge = Edge(self.rooms[0], self.rooms[1])
        mst = []

        while len(seenRooms) < MapConstants.TOTAL_ROOMS:

            availableEdges = []
            for seenRoom in seenRooms:
                for edge in seenRoom.edges:

                    if edge.rooms[0] in seenRooms and edge.rooms[1] not in seenRooms:
                        availableEdges.append( edge )

            minimumEdge = min( availableEdges, key=lambda edge: edge.weight, default=defaultEdge)
            seenRooms.append( minimumEdge.rooms[1] )
            mst.append(minimumEdge)

            # Throw random edges in
            while (random.random() < MapConstants.CHANCE_FOR_NEW_EDGE and len(availableEdges) != 0):
                
                randomEdge = random.choice(availableEdges)
                # Max of 6 room connections per room
                if (len(randomEdge.rooms[0].getAdjacentRooms()) < 6 and len(randomEdge.rooms[1].getAdjacentRooms()) < 6):
                    mst.append( randomEdge)

        # From what was created from prim's algorithm, create adjacency between rooms
        # Edges and adjacency are kinda redundant tbh
        for edge in mst:
            edge.rooms[0].createAdjacency(edge.rooms[1])

        # Create Start room
        MapConstants.START_ROOM.addAdjacentRoom(self.rooms[0])
        

    def assignRandomImages(self):
        button_images = [ "Weapons Bay", "Main Cabin", "Elevator 1", "Storage Area", "Kitchen", "Barracks", "Cafeteria",
            "Life Pod 1", "Cabin 2", "Showers", "Cabin 1", "Docking Port", "Bridge", "Elevator 3", "Elevator 2", "Cabin 3",
            "Captains Cabin", "Hangar", "Life Pod 2", "Engine Room"]
        
        random.shuffle( button_images )

        for room in self.rooms:
            room.setImagePath(f"Map/Set/{button_images.pop()}.jpg")

    def printMap(self):
        print(f"{MapConstants.START_ROOM} is adjacent to: {MapConstants.START_ROOM.getAdjacentRooms()}\n\n")
        for room in self.rooms:
            print(f"{room} is adjacent to: {room.getAdjacentRooms()}\n\n")
        