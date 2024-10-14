from lib.user import *
from unittest.mock import Mock
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
    fake_receipt = Mock()
    user = User(fake_receipt)
    assert isinstance(user, User)
    assert user.receipt == fake_receipt

def test_view_menu():
    fake_receipt = Mock()
    user = User(fake_receipt)
    fake_receipt.takeaway.menu = menu
    result = user.view_menu()
    assert result == menu

"""
Not really sure if the test below has any point 
How would I test this with mocks if all this does is call
- a method in the mock that effects an attribute in the mock
"""

def test_order():
    fake_receipt = Mock()
    user = User(fake_receipt)
    fake_receipt.items_ordered = {'total': 9.5, 'chicken butterfly': {'price': 9.5, 'quantity': 1}}
    user.order('chicken butterfly')
    assert fake_receipt.items_ordered == {'total': 9.5, 'chicken butterfly': {'price': 9.5, 'quantity': 1}}

def test_order_for_a_non_string():
    fake_receipt = Mock()
    user = User(fake_receipt)
    with pytest.raises(Exception) as e:
        user.order(20)
    error_message = str(e.value)
    assert error_message == 'Only works with strings'

def test_remove_for_a_non_string():
    fake_receipt = Mock()
    user = User(fake_receipt)
    with pytest.raises(Exception) as e:
        user.remove_order(20)
    error_message = str(e.value)
    assert error_message == 'Only works with strings'

def test_remove_order():
    fake_receipt = Mock()
    user = User(fake_receipt)
    user.order('chicken butterfly')
    user.remove_order('chicken butterfly')
    fake_receipt.items_ordered = {'total': 0}
    assert fake_receipt.items_ordered == {'total': 0}    

def test_remove_order_that_is_not_in_order():
    fake_receipt = Mock()
    user = User(fake_receipt)
    user.order('chicken butterfly')
    fake_receipt.items_ordered = {'total': 9.5, 'chicken butterfly': {'price': 9.5, 'quantity': 1}}
    user.remove_order('hamburger')
    assert fake_receipt.items_ordered == {'total': 9.5, 'chicken butterfly': {'price': 9.5, 'quantity': 1}}

def test_request_bill():
    fake_receipt = Mock()
    user = User(fake_receipt)
    user.order('chicken butterfly')
    user.order('wing roulette')
    user.order('chicken butterfly')
    fake_receipt.view_receipt.return_value = 'chicken butterfly * 2 = 19.\nwing roulette * 1 = 12.25.\nTotal = 31.25'
    assert user.request_bill() == 'chicken butterfly * 2 = 19.\nwing roulette * 1 = 12.25.\nTotal = 31.25'

