from classes.rooms import Rooms
# from classes.CodeClan_Caraoke import CodeClan_Caraoke
import unittest
from classes.guests import Guests
# from classes.songs import songs

class RoomTest(unittest.TestCase):

    def setUp(self):
        self.room1 = Rooms("90's pop room", 50)
        self.room2 = Rooms("rocker's room", 25)

    def test_room_has_name(self):
        self.assertEqual("90's pop room" , self.room1.name) 
        self.assertEqual("rocker's room" , self.room2.name) 
    
    def test_room_has_price(self):
        self.assertEqual(50, self.room1.price)



