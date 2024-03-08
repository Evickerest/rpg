from Classes.Rooms.BossRoom import BossRoom
from Classes.Rooms.ChestRoom import ChestRoom
from Classes.Rooms.ShopRoom import ShopRoom
from Classes.Rooms.CombatRoom import CombatRoom
from Classes.Rooms.StartRoom import StartRoom

class MapConstants:
    TOTAL_ROOMS = 15
    CHANCE_FOR_NEW_EDGE = 0.25
    START_ROOM = StartRoom()

    ROOM_TYPES = {
        "Combat": {
            "desired_number": 10,
            "room": CombatRoom
        },
        "Chest": {
            "desired_number": 2,
            "room": ChestRoom
        },
        "Shop": {
            "desired_number": 2,
            "room": ShopRoom
        },
        "Boss": {
            "desired_number": 1,
            "room": BossRoom
        }

    }