"""Module for the Map class.
"""

import random
from Classes.Map.edge import Edge
from Classes.Map.mapconstants import MapConstants
from Classes.Rooms.start_room import StartRoom

# Manages the rooms and room connections


class Map:
    """Contains multiple Room instances and connects them together.
    """
    def __init__(self):
        """Creates the Map instance.
        """
        self.rooms = None
        self.current_room = None
        self.edges = []
        self.start_room = StartRoom()

        self.generate_map()

    def generate_map(self):
        """Method to generate the map.
        """
        self.generate_random_rooms()
        self.connect_every_room_together()
        self.prims_algorithm()
        self.set_current_room(self.start_room)
        self.assign_random_images()
        # self.printMap()

    def get_current_room(self):
        """Getter for the current room of the map.
        Returns:
            current_room (Room): The Room the player is in.
        """
        return self.current_room

    def set_current_room(self, room):
        """Setter for the current room of the map.
        Args:
            room (Room): The Room instance to set as the currentRoom.
        """
        self.current_room = room

    def generate_random_rooms(self):
        """Method to generate random rooms.
        """
        self.rooms = []

        counter = 1
        # Loop through each room type
        for room_type in MapConstants.ROOM_TYPES:
            # Loop for the desired number of rooms
            for _ in range(
                    MapConstants.ROOM_TYPES[room_type]["desired_number"]):
                random_x = random.random()
                random_y = random.random()

                # Create room and set coordinates
                room = MapConstants.ROOM_TYPES[room_type]["room"]()
                # room.image = randomImage()

                room.number = str(counter)
                counter += 1

                room.set_coordinates(random_x, random_y)

                self.rooms.append(room)

    # Create an edge between all possible pairs of rooms
    def connect_every_room_together(self):
        """Method to create edges between rooms.
        """
        for room in self.rooms:
            for other_room in self.rooms:
                if room != other_room:
                    room.edges.append(Edge(room, other_room))

    # Implementation of Prim's Algorithm
    # Takes a graph of nodes (rooms) and edges, and constructs a minimum
    # spanning tree. Downside is that a mst doesn't produce cycles, so
    # additional edges will have to be added in.
    def prims_algorithm(self):
        """Method to create a minimum spanning tree to connect all
         rooms together.
        """
        seen_rooms = [self.rooms[0]]
        default_edge = Edge(self.rooms[0], self.rooms[1])
        mst = []

        while len(seen_rooms) < MapConstants.TOTAL_ROOMS:

            available_edges = []
            for seenroom in seen_rooms:
                for edge in seenroom.edges:

                    if (edge.rooms[0] in seen_rooms and edge.rooms[1]
                            not in seen_rooms):
                        available_edges.append(edge)

            minimum_edge = min(available_edges, key=lambda edge: edge.weight,
                               default=default_edge)
            seen_rooms.append(minimum_edge.rooms[1])
            mst.append(minimum_edge)

            # Throw random edges in
            while (random.random() < MapConstants.CHANCE_FOR_NEW_EDGE
                   and len(available_edges) != 0):

                random_edge = random.choice(available_edges)
                # Max of 6 room connections per room
                if (len(random_edge.rooms[0].get_adjacent_rooms()) < 6 and
                        len(random_edge.rooms[1].get_adjacent_rooms()) < 6):
                    mst.append(random_edge)

        # From what was created from Prim's algorithm, create adjacency between
        # rooms.
        # Edges and adjacency are kinda redundant tbh
        for edge in mst:
            edge.rooms[0].create_adjacency(edge.rooms[1])

        # Create Start room
        self.start_room.add_adjacent_room(self.rooms[0])
        self.start_room.cleared = True

    def assign_random_images(self):
        """Method to assign an image path to all rooms in the map.
        """
        from Classes.game_handler import GameHandler  # To import the Level counter from GameHandler
        self.lvl_counter = GameHandler.counter
        button_images1 = ["Weapons Bay", "Main Cabin", "Elevator 1",
                          "Storage Area", "Kitchen", "Barracks", "Cafeteria",
                          "Life Pod 1", "Cabin 2", "Showers", "Cabin 1",
                          "Docking Port", "Bridge", "Elevator 3", "Elevator 2",
                          "Cabin 3", "Captains Cabin", "Hangar", "Life Pod 2",
                          "Engine Room"]
        button_images2 = ['A-1', 'A-2', 'Access Shaft', 'Access Shaft 2',
                          'Access Shaft 3', 'Arms Room', 'Bridge 1',
                          'Bridge 2', 'C-1', 'C-2', 'Command Module', 'Computer',
                          'Freezer', 'Infirmary', 'Lab', 'Living Quarters',
                          'Mess', 'Power', 'Shuttle Dock 1', 'Shuttle Dock 2', 'Storage',
                          'Storage 2', 'Storage 3', 'Main Airlock']


        if self.lvl_counter == 1:
            random.shuffle(button_images1)
            for room in self.rooms:
                room.set_image_path(f"Images/LevelOneMap/Set/{button_images1.pop()}.jpg")


        elif self.lvl_counter == 2:
            random.shuffle(button_images2)
            for room in self.rooms:
                room.set_image_path(f"Images/LevelTwoMap/{button_images2.pop()}.jpg")

    def print_map(self):
        """Method to print all the rooms in the map and their adjacent rooms.
        """
        print(f"{self.start_room} is adjacent to:"
              f" {self.start_room.get_adjacent_rooms()}\n\n")
        for room in self.rooms:
            print(f"{room} is adjacent to: {room.get_adjacent_rooms()}\n\n")
