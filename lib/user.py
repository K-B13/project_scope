class User:
    def __init__(self, receipt):
        self.receipt = receipt

    def view_menu(self):
        return self.receipt.takeaway.menu
    
    def order(self, dish):
        if type(dish) != str:
            raise Exception('Only works with strings')
        self.receipt.add_item(dish)

    def remove_order(self, dish):
        if type(dish) != str:
            raise Exception('Only works with strings')
        self.receipt.remove_item(dish)

    def request_bill(self):
        return self.receipt.view_receipt()