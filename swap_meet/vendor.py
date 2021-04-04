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
