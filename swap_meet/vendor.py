from .item import Item
import operator

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
            other_vendor.add(item_a)
            self.remove(item_a)
            other_vendor.remove(item_b)
            self.add(item_b)
            return True
        else:
            return False
        
    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        else:
            return False
    
    def get_best_by_category(self, category):
        '''first calls get_by_category module
            sorts items low to high by condition using operator.attrgetter'''

        items = self.get_by_category(category)
        if len(items) == 0:
            return None

        sorted_items = sorted(items, key=operator.attrgetter('condition'))
        return sorted_items[-1]
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        vendor_best = self.get_best_by_category(their_priority)
        other_vendor_best = other.get_best_by_category(my_priority)
        if other_vendor_best and vendor_best:
            return self.swap_items(other, vendor_best, other_vendor_best)
        else:
            return False
        



            
            
                
        
        

