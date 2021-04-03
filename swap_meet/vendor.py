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
            if item_a in self.inventory and item_b in vendor.inventory:
                self.remove(item_a)
                vendor.add(item_a)
                self.add(item_b)
                vendor.remove(item_b)
            else: 
                return False
            return True
    
    def swap_first_item(self, vendor):
        if len(self.inventory) >= 1 and len(vendor.inventory)>= 1:
            self_first_item = self.inventory[0]
            print(self_first_item)
            vendor_first_item = vendor.inventory[0]
            print(self_first_item)
        else:
            return False
        vendor.add(self_first_item)
        self.add(vendor_first_item)
        vendor.remove(vendor_first_item)
        self.remove(self_first_item)
        return True







