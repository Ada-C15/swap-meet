# from swap_meet.vendor import Vendor

class Vendor:
    def __init__(self, inventory = []): 
        self.inventory = inventory      # instances
         
        
    def add(self, item):   # adds item to inventory and returns item
        self.inventory.append(item)
        return item
            
    def remove(self, item): # removes item from inventory and returns item
        if item not in (self.inventory):
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

