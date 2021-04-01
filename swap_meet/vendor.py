from .item import Item

# WAVE 1

class Vendor:

    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

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

    def swap_items(self, vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        # if my_item in self.inventory:
        self.remove(my_item)
        vendor.add(my_item)

        
        # if their_item in vendor.inventory:
        vendor.remove(their_item)
        self.add(their_item)

        return True





