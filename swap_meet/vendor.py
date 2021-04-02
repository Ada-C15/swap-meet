# from swap_meet.vendor import Vendor

class Vendor:
    def __init__(self, inventory = None): 
        if inventory == None:
            self.inventory = []      # instances
        else:
            self.inventory = inventory
            
        
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

    
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory:
            return False
        if their_item not in friend.inventory:
            return False 
        
        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)
        self.add(their_item)
        return True 

        
        
