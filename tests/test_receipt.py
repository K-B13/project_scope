from lib.receipt import *
from unittest.mock import Mock
import pytest


def test_initialisation():
    fake_takeaway = Mock()
    receipt = Receipt(fake_takeaway)

    assert isinstance(receipt, Receipt)
    assert receipt.takeaway == fake_takeaway
    assert receipt.items_ordered == {'total': 0}


def test_add_item_first_item_added_and_item_on_menu():
    fake_takeaway = Mock()
    fake_takeaway.find_dish.side_effect = lambda dish: 9.5 if dish == 'chicken butterfly' else None
    receipt = Receipt(fake_takeaway)
    receipt.add_item('chicken butterfly')
    assert receipt.items_ordered == {'total': 9.5, 'chicken butterfly': {'price': 9.5, 'quantity': 1}}

def test_add_item_more_than_one_of_single_item():
    fake_takeaway = Mock()
    fake_takeaway.find_dish.side_effect = lambda dish: 9.5 if dish == 'chicken butterfly' else None
    receipt = Receipt(fake_takeaway)
    receipt.add_item('chicken butterfly')
    receipt.add_item('chicken butterfly')
    assert receipt.items_ordered == {'total': 19.0, 'chicken butterfly': {'price': 9.5, 'quantity': 2}}

def test_add_item_not_on_menu():
    fake_takeaway = Mock()
    fake_takeaway.find_dish.side_effect = mock_find_dish
    receipt = Receipt(fake_takeaway)
    receipt.add_item('chicken butterfly')
    with pytest.raises(Exception) as e:
        receipt.add_item('noodles')
    error_message = str(e.value)    
    assert error_message == 'noodles is not on the menu'

def mock_find_dish(dish):
    if dish == 'chicken butterfly':
        return 9.5
    else:
        raise Exception(f"{dish} is not on the menu")


def test_add_item_more_than_one_different_items():
    fake_takeaway = Mock()
    fake_takeaway.find_dish.side_effect = lambda dish: 9.5 if dish == 'chicken butterfly' else 12.25
    receipt = Receipt(fake_takeaway)
    receipt.add_item('chicken butterfly')
    receipt.add_item('wing roulette')
    assert receipt.items_ordered == {'total': 21.75, 'chicken butterfly': {'price': 9.5, 'quantity': 1}, 'wing roulette': {'price': 12.25, 'quantity': 1}}

def test_remove_from_empty_receipt():
    fake_takeaway = Mock()
    receipt = Receipt(fake_takeaway)
    with pytest.raises(Exception) as e:
        receipt.remove_item('chicken butterfly')
    error_message = str(e.value)
    assert error_message == 'chicken butterfly is not in your order'

def test_remove_from_one_item_receipt():
    fake_takeaway = Mock()
    receipt = Receipt(fake_takeaway)
    fake_takeaway.find_dish.side_effect = lambda dish: 9.5 if dish == 'chicken butterfly' else 12.25
    receipt.add_item('chicken butterfly')
    receipt.remove_item('chicken butterfly')
    assert receipt.items_ordered == {'total': 0}

def test_remove_from_more_than_one_item_receipt():
    fake_takeaway = Mock()
    receipt = Receipt(fake_takeaway)
    fake_takeaway.find_dish.side_effect = lambda dish: 9.5 if dish == 'chicken butterfly' else 12.25
    receipt.add_item('chicken butterfly')
    receipt.add_item('wing roulette')
    receipt.remove_item('chicken butterfly')
    assert receipt.items_ordered == {'total': 12.25,  'wing roulette': {'price': 12.25, 'quantity': 1}}

def test_remove_when_more_than_one_of_single_item():
    fake_takeaway = Mock()
    receipt = Receipt(fake_takeaway)
    fake_takeaway.find_dish.side_effect = lambda dish: 9.5 if dish == 'chicken butterfly' else 12.25
    receipt.add_item('chicken butterfly')
    receipt.add_item('chicken butterfly')
    receipt.remove_item('chicken butterfly')
    assert receipt.items_ordered == {'total': 9.5, 'chicken butterfly': {'price': 9.5, 'quantity': 1}}

def test_view_receipt_when_empty():
    fake_takeaway = Mock()
    receipt = Receipt(fake_takeaway)
    bill = receipt.view_receipt()
    assert bill == 'Empty.\nTotal = 0'

def test_view_receipt_with_one_item():
    fake_takeaway = Mock()
    receipt = Receipt(fake_takeaway)
    fake_takeaway.find_dish.side_effect = lambda dish: 9.5 if dish == 'chicken butterfly' else 12.25
    receipt.add_item('chicken butterfly')
    bill = receipt.view_receipt()
    assert bill == 'chicken butterfly * 1 = 9.5.\nTotal = 9.5'

def test_view_receipt_with_multiple_different_items():
    fake_takeaway = Mock()
    receipt = Receipt(fake_takeaway)
    fake_takeaway.find_dish.side_effect = lambda dish: 9.5 if dish == 'chicken butterfly' else 12.25
    receipt.add_item('chicken butterfly')
    receipt.add_item('chicken butterfly')
    receipt.add_item('chicken butterfly')
    receipt.add_item('wing roulette')
    receipt.add_item('wing roulette')
    bill = receipt.view_receipt()
    assert bill == 'chicken butterfly * 3 = 28.5.\nwing roulette * 2 = 24.5.\nTotal = 53.0'