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
        self.swap_items(vendor, self_first_item, vendor_first_item)
        return True

    def get_best_by_category(self, category):
        best_condition = 0
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition >= best_condition:
                    best_condition += item.condition
                    best_item = item    
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        self_wants = other.get_best_by_category(my_priority)

        vendor_wants = self.get_best_by_category(their_priority)
        if vendor_wants == None or self_wants == None:
            return False
        else:
            self.swap_items(other, vendor_wants, self_wants)
            return True
        
                
    
    









