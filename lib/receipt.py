class Receipt:
    def __init__(self, takeaway):
        self.items_ordered = {'total': 0}
        self.takeaway = takeaway

    def add_item(self, dish_name):
        item = self.takeaway.find_dish(dish_name)
        if item == None:
            raise Exception(f"{dish_name} is not on the menu")
        already_ordered = [dish for dish in self.items_ordered if dish == dish_name]
        if len(already_ordered) == 0:
            self.items_ordered[dish_name] = {'price': item, 'quantity': 1}
        else:
            self.items_ordered[dish_name]['quantity'] += 1
        self.items_ordered['total'] += item

    def remove_item(self, dish_name):
        already_ordered = [dish for dish in self.items_ordered if dish == dish_name]
        if len(already_ordered) == 0:
            raise Exception(f"{dish_name} is not in your order")
        dish_details = self.items_ordered[dish_name]
        self.items_ordered['total'] -= dish_details['price']
        if dish_details['quantity'] > 1:
            dish_details['quantity'] -= 1
        else:
            del self.items_ordered[dish_name]

    def view_receipt(self):
        bill = self._format_receipt()
        return bill

    def _format_receipt(self):
        bill_msg = ''
        end_total = ''
        for dish, value in self.items_ordered.items():
            if dish == 'total':
                end_total += f"{dish.capitalize()} = {value}"
                continue
            bill_msg += f"{dish} * {value['quantity']} = {value['quantity'] * value['price']}.\n"
        if bill_msg == '':
            bill_msg = 'Empty.\n'
        return bill_msg + end_total