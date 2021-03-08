class Guests:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def pay (self, amount):
        self.wallet -= amount

    def buy_drink(self, drink):
        self.wallet -= drink.price