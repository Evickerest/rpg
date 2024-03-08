from Classes.Rooms.Room import Room

class StartRoom(Room):
    def __init__(self):
        super().__init__()
        self.name = "Start"
        self.roomType = "Start"
        self.text = "You are in the start room."
