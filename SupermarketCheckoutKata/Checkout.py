class Checkout:

    def __init__(self):
        self.prices = {}
        self.total = 0

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        self.total += self.prices[item]

    def calculateTotal(self):
        return self.total
