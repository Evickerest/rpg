from Classes.Rooms.ChestRoom import ChestRoom
from Classes.Rooms.ShopRoom import ShopRoom
from Classes.Rooms.CombatRoom import CombatRoom

class MapConstants:
    TOTAL_ROOMS = 20

    # Completely Arbitrary
    MAP_HEIGHT = 50
    MAP_WIDTH = 50

    ROOM_TYPES = {
        "Combat": {
            "desired_number": 10,
            "room": CombatRoom
        },
        "Chest": {
            "desired_number": 9,
            "room": ChestRoom
        },
        "Shop": {
            "desired_number": 1,
            "room": ShopRoom
        }
    }

    CHANCE_FOR_NEW_EDGE = 0.2
