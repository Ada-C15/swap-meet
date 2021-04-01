from .item import Item
# Create a vendor class that has an inventory attribute 
# the inventory attribute can come as a parameter but should not be required 

class Vendor: 
    def __init__(self, inventory = None):
        if inventory == None:
                self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        
        return item 
    
    def get_by_category(self, category):
        item_by_category = []
        for item in self.inventory:
            if item.category == category:
                item_by_category.append(item)
        return item_by_category

    def swap_items(self, vendor, item_a, item_b):
        for item in self.inventory:
            if item == item_a:
                self.remove(item)
                vendor.add(item)
                print(self.inventory)
                print(vendor.inventory)
                if item_b not in vendor.inventory:
                    return False
                else:
                    self.add(item_b)
                    vendor.remove(item_b)
                    return True
            else:
                return False
        return True







