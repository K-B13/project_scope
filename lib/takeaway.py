class Takeaway:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def show_menu(self):
        return self.menu
    
    def find_dish(self, dishname):
        if type(dishname) != str:
            return None
        return self.menu.get(dishname)