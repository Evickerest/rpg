# Store room information for current stage of game

class Map:
    def __init__(self, rooms):
        self.rooms = rooms

    def setAdjacentRoom(self, room, otherRoom ):
        room.setRoomAsAdjacent(otherRoom)

    def getAdjacentRooms(self, nameOfRoom):
        return self.rooms[nameOfRoom].adjacentRooms
    
    def getRoomByName(self, name):
        return self.rooms[name]

        
