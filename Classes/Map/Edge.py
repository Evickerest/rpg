import math

class Edge:
    def __init__(self, room1, room2):
        self.rooms = (room1, room2)
        self.weight = math.dist(room1.getCoordinates(), room2.getCoordinates())
    def getWeight(self):
        return self.weight
    def __repr__(self):
        return f"{self.rooms[0]} <-> {self.rooms[1]} | {self.weight}"
                      