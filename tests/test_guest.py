import unittest

from classes.guests import Guests

class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer = Guests("Buddha", 300)
        # self.customer = Guests("jonny", 150)
        # self.customer = Guests("sAriana", 100)

    def test_pay__reduces_money(self):
        self.customer.pay(30)
        self.assertEqual(270,self.customer.wallet) 