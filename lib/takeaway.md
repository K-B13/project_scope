# User Stories
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.
# Could have a takeaway class that has the menu which will be a dictionary
# I could have separate dictionaries within for starters, mains, desserts and sides
# Each of those will have name as key and price as the value
# Will need a method for showing the menu

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.
# Will need a method for finding dishes within the dictionary. Look into multiple arguments

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.
# Will need a list of dictionaries of the items they choose each item will be a dictionary with
# -- name, cost and quantity as keys
# Method called see_bill which formats the above dictionary in a different format and calculates the see_bill


# Optional Extra
As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.


class TakeAway:
    def __init__(self):
        _menu: dictionary with name and value
    
    def show_menu(self):
        return self._menu

    def find_dish(self, dish_name):
        return dish

class Receipt:
    def __init__(self, takeaway):
        items_ordered = {total = 0}
        receipt_from: takeaway

    def add_item(self, item):
        finds item in takaway
        run _locate_dish
        append item to order or increase quantity
        increase total

    def _locate_dish(self, item):
        checks if item in items_ordered
        returns item or False if not in

    def remove_item(self, item):
        run _locate_dish
        check quantity
        if one remove it else decrement it
        decrease total

    def view_receipt(self):
        run _format_bill
        return bill
    
    def _format_receipt(self):
        returns formatted_bill

class User:
    def__init__(self, receipt):
        receipt: Receipt

    def view_menu(self):
        return receipt.takeaway.show_menu()

    def order(self, dishname):
        runs receipt.add_item

    def remove_order(self, dishname):
        runs receipt.remove_item
    
    def request_bill(self):
        runs 

    