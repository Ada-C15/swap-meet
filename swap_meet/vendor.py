class Vendor:

    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory 

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False