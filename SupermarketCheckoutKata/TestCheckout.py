from Checkout import Checkout

def test_CantInstantiateCheckout():
    co = Checkout()

def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice("a", 1)