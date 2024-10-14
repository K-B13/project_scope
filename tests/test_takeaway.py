from lib.takeaway import *
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
    assert isinstance(takeaway, Takeaway)
    assert takeaway.name == 'Nandos'
    assert takeaway.menu == menu

def test_show_menu():
    takeaway = Takeaway('Nandos', menu)
    result = takeaway.show_menu()
    assert result == menu

def test_find_dish_with_dish_in_menu():
    takeaway = Takeaway('Nandos', menu)
    result = takeaway.find_dish('chicken butterfly')
    assert result == 9.5

def test_find_dish_with_dish_not_in_menu():
    takeaway = Takeaway('Nandos', menu)
    result = takeaway.find_dish('noodles')
    assert result == None

def test_find_dish_with_dish_no_string():
    takeaway = Takeaway('Nandos', menu)
    result = takeaway.find_dish([])
    assert result == None
