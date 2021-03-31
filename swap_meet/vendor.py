from .item import Item

# WAVE 1

class Vendor:
    
    # copy of list?
    def __init__(self, inventory = []):
        self.inventory = list(inventory)

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):

        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        
        matching_category_list = []

        for item in self.inventory:
            if item.category == category:
                matching_category_list.append(item)
        
        return matching_category_list



