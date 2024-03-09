"""Module for the Map class.
"""

import math
import random
from Classes.Character import *
from Classes.Map.Edge import Edge
from Classes.Map.MapConstants import MapConstants

# Manages the rooms and room connections


class Map:
    """Contains multiple Room instances and connects them together.
    """
    def __init__(self):
        """Creates the Map instance.
        """
        self.rooms = None
        self.currentRoom = None
        self.edges = []

        self.generate_map()

    def generate_map(self):
        """Method to generate the map.
        """
        self.generate_random_rooms()
        self.connect_every_room_together()
        self.prims_algorithm()
        self.set_current_room(MapConstants.START_ROOM)
        self.assign_random_images()
        # self.printMap()

    def get_current_room(self):
        """Getter for the current room of the map.
        Returns:
            currentRoom (Room): The Room the player is in.
        """
        return self.currentRoom
    
    def set_current_room(self, room):
        """Setter for the current room of the map.
        Args:
            room (Room): The Room instance to set as the currentRoom.
        """
        self.currentRoom = room

    def generate_random_rooms(self):
        """Method to generate random rooms.
        """
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

                room.set_coordinates(randomX, randomY)

                self.rooms.append(room)

    # Create an edge between all possible pairs of rooms
    def connect_every_room_together(self):
        """Method to create edges between rooms.
        """
        for room in self.rooms:
            for otherRoom in self.rooms:
                if room != otherRoom:
                    room.edges.append(Edge(room, otherRoom))

    # Implementation of Prim's Algorithm
    # Takes a graph of nodes (rooms) and edges, and constructs a minimum spanning tree
    # Downside is that a mst doesn't produce cycles, so additional edges will have to be added in              
    def prims_algorithm(self):
        """Method to create a minimum spanning tree to connect all rooms together.
        """
        seenRooms = [self.rooms[0]]
        defaultEdge = Edge(self.rooms[0], self.rooms[1])
        mst = []

        while len(seenRooms) < MapConstants.TOTAL_ROOMS:

            availableEdges = []
            for seenRoom in seenRooms:
                for edge in seenRoom.edges:

                    if edge.rooms[0] in seenRooms and edge.rooms[1] not in seenRooms:
                        availableEdges.append(edge)

            minimumEdge = min(availableEdges, key=lambda edge: edge.weight, default=defaultEdge)
            seenRooms.append(minimumEdge.rooms[1])
            mst.append(minimumEdge)

            # Throw random edges in
            while (random.random() < MapConstants.CHANCE_FOR_NEW_EDGE and len(availableEdges) != 0):
                
                randomEdge = random.choice(availableEdges)
                # Max of 6 room connections per room
                if (len(randomEdge.rooms[0].get_adjacent_rooms()) < 6 and
                        len(randomEdge.rooms[1].get_adjacent_rooms()) < 6):
                    mst.append(randomEdge)

        # From what was created from prim's algorithm, create adjacency between rooms
        # Edges and adjacency are kinda redundant tbh
        for edge in mst:
            edge.rooms[0].create_adjacency(edge.rooms[1])

        # Create Start room
        MapConstants.START_ROOM.add_adjacent_room(self.rooms[0])

    def assign_random_images(self):
        """Method to assign an image path to all rooms in the map.
        """
        button_images = ["Weapons Bay", "Main Cabin", "Elevator 1", "Storage Area", "Kitchen",
                         "Barracks", "Cafeteria", "Life Pod 1", "Cabin 2", "Showers", "Cabin 1",
                         "Docking Port", "Bridge", "Elevator 3", "Elevator 2", "Cabin 3",
                         "Captains Cabin", "Hangar", "Life Pod 2", "Engine Room"]
        
        random.shuffle(button_images)

        for room in self.rooms:
            room.set_image_path(f"Map/Set/{button_images.pop()}.jpg")

    def print_map(self):
        """Method to print all the rooms in the map and their adjacent rooms.
        """
        print(f"{MapConstants.START_ROOM} is adjacent to: {MapConstants.START_ROOM.get_adjacent_rooms()}\n\n")
        for room in self.rooms:
            print(f"{room} is adjacent to: {room.get_adjacent_rooms()}\n\n")
        