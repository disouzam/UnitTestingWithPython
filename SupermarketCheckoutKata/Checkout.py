class Checkout:

    def __init__(self):
        self.prices = {}
        self.total = 0

    def addDiscount(self, item, nbrOfItems, price):
        pass


    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        self.total += self.prices[item]

    def calculateTotal(self):
        return self.total
