from classes.rooms import Rooms
from classes.CodeClan_Caraoke import CodeClan_Caraoke
import unittest
from classes.guests import guests
# from classes.songs import songs

class ThemeParkTest(unittest.TestCase):

    def setUp(self):
        self.guests = guests("Buddha", 1000)
        self.Room = room ("90's pop room", 50)
        self.Room = room ("rocker's room", 25)

        Rooms = [self.room1, self.room2]

        self.CodeClan_Caraoke = CodeClan_Caraoke("CodeClan_Caraoke", Rooms)

    def test_can_sell_ticket_for_entry(self):
        self.theme_park.sell_ticket_for_ride(self.room1, self.customer)

        self.assertEqual(50, self.CodeClan_Caraoke.total_income)
        self.assertEqual(950, self.customer.wallet)
