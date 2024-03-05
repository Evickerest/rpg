from Classes.Rooms.ChestRoom import ChestRoom
from Classes.Rooms.ShopRoom import ShopRoom
from Classes.Rooms.CombatRoom import CombatRoom

class MapConstants:
    TOTAL_ROOMS = 50

    # Completely Arbitrary
    MAP_HEIGHT = 50
    MAP_WIDTH = 50

    ROOM_TYPES = {
        "Combat": {
            "desired_number": 35,
            "room": CombatRoom
        },
        "Chest": {
            "desired_number": 10,
            "room": ChestRoom
        },
        "Shop": {
            "desired_number": 5,
            "room": ShopRoom
        }
    }