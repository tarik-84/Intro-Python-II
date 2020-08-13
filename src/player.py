# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player1:
    def __init__(self, current_room):
        # Store current_room as a Room object
        self.current_room: Room = current_room
class Player2:
    def __init__(self, current_room):
        # Store current_room as a string (key into the room dict in adv.py)
        self.current_room: str = current_room