from lib.takeaway import *
from lib.receipt import *
from lib.user import *
import pytest

menu = {
    'chicken butterfly': 9.50,
    'wing roulette': 12.25,
    'whole chicken': 15.95,
    'butterfly burger': 11.75,
    'grilled chicken burger': 7.95,
    'full platter': 26.75,
    'beanie wrap': 7.95,
    'chips': 3.85,
    'double chicken pitt': 11.75,
    'sweet potato wedges': 4.75
}

def test_initialisation():
    takeaway = Takeaway('Nandos', menu)
    receipt = Receipt(takeaway)
    user = User(receipt)
    assert user.receipt == receipt
    assert user.receipt.takeaway == takeaway
    
def test_order_three_different_items():
    takeaway = Takeaway('Nandos', menu)
    receipt = Receipt(takeaway)
    user = User(receipt)
    user.order('butterfly burger')
    user.order('chips')
    user.order('chips')
    user.order('whole chicken')
    result = user.request_bill()
    assert result == 'butterfly burger * 1 = 11.75.\nchips * 2 = 7.7.\nwhole chicken * 1 = 15.95.\nTotal = 35.4' 

def test_order_a_lot_of_different_items_and_remove_a_few():
    takeaway = Takeaway('Nandos', menu)
    receipt = Receipt(takeaway)
    user = User(receipt)
    user.order('butterfly burger')
    user.order('chips')
    user.order('chips')
    user.order('whole chicken')
    user.order('wing roulette')
    user.order('whole chicken')
    user.order('grilled chicken burger')
    user.order('whole chicken')
    user.remove_order('whole chicken')
    user.remove_order('butterfly burger')
    result = user.request_bill()
    assert result == 'chips * 2 = 7.7.\nwhole chicken * 2 = 31.9.\nwing roulette * 1 = 12.25.\ngrilled chicken burger * 1 = 7.95.\nTotal = 59.8' 

def test_view_menu():
    takeaway = Takeaway('Nandos', menu)
    receipt = Receipt(takeaway)
    user = User(receipt)
    result = user.view_menu()
    assert result == menu

def test_dish_that_is_not_on_menu():
    takeaway = Takeaway('Nandos', menu)
    receipt = Receipt(takeaway)
    user = User(receipt)
    with pytest.raises(Exception) as e:
        user.order('fried chicken')
    error_message = str(e.value)
    assert error_message == 'fried chicken is not on the menu'

def test_remove_dish_that_is_not_in_order():
    takeaway = Takeaway('Nandos', menu)
    receipt = Receipt(takeaway)
    user = User(receipt)
    user.order('chips')
    with pytest.raises(Exception) as e:
        user.remove_order('fried chicken')
    error_message = str(e.value)
    assert error_message == 'fried chicken is not in your order'    

