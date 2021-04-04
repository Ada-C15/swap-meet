from .item import Item 

#Wave 1
# the attributes are the list of items/invetory and the class is vendor

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
        return

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
        
    def swap_items(self, vendor,  my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:  

            self.remove(my_item)
            vendor.add(my_item) 
            vendor.remove(their_item)
            self.add(their_item)
            return True  
        return False


    def swap_first_item(self, vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        return False 

    def get_best_by_category(self, category):
        highest_condition_item = Item(category)
        item_exists = False
        for item in self.inventory:
            if item.category == category and item.condition > highest_condition_item.condition:
                highest_condition_item = item 
                item_exists = True
        if not item_exists: return None
        return highest_condition_item


    def swap_best_by_category(self, other, my_priority,their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if my_item == None or their_item == None:
            return False 
        return self.swap_items(other, my_item, their_item)