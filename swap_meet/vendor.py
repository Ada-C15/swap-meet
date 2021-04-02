from .item import Item

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
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, other_vendor, item_a, item_b):
        if item_a in self.inventory and item_b in other_vendor.inventory:
            other_vendor.inventory.append(item_a)
            self.inventory.remove(item_a)
            other_vendor.inventory.remove(item_b)
            self.inventory.append(item_b)
            return True
        else:
            return False
        
    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            temp = other_vendor.inventory[0]
            other_vendor.inventory[0] = self.inventory[0]
            self.inventory[0] = temp
            return True
        else:
            return False
    
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        else:
            best_item = items[0]
        for item in items:
            if item.condition >= best_item.condition:
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        vendor_best = self.get_best_by_category(their_priority)
        other_vendor_best = other.get_best_by_category(my_priority)
        self.swap_items(other, vendor_best, other_vendor_best)
        return True



            
            
                
        
        

