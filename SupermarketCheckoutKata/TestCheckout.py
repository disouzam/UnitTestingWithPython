import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

# Tests removed by instructor Richard Wells since in his view they are not necessary anymore
# though I prefer to have a slight duplication but to assert properly that those actions
# are correctly performed
# def test_CanAddItemPrice(checkout):
#     checkout.addItemPrice("a", 1)
#
# def test_CanAddItem(checkout):
#     checkout.addItem("a")

def test_CanCalculateTotal(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItemPrice("a",1)
    checkout.addItemPrice("b",2)
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
