from swap_meet.item import Item

class Vendor: 
    def __init__(self, inventory=None):
        if inventory == None: 
            self.inventory = []
        else: 
            self.inventory = inventory

    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item    
    
    def remove(self, rm_item): 
        if rm_item in self.inventory:
            self.inventory.remove(rm_item)
            return rm_item
        else:
            return rm_item  == False 
    
    def get_by_category(self, asked_category):
        item_list =[]
        for item in self.inventory: 
            if item.category == asked_category:
                item_list.append(item)
        
        return item_list
    
    def swap_items(self, other_vendor, my_item, their_item): 
        if my_item in self.inventory and their_item in other_vendor.inventory: 
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True 
        else: 
            return False

    def swap_first_item(self, other_vendor): 
        if len(self.inventory) and len(other_vendor.inventory) > 0: 
            self_inventory_1 = self.inventory[0]  
            other_vendor_invetory_1 = other_vendor.inventory[0]
            return self.swap_items(other_vendor, self_inventory_1, other_vendor_invetory_1)
        else: 
            return False
    
    def get_best_by_category(self, category): 
        item_list = self.get_by_category(category)
        initial_condition = 0.0
        best_item = None

        if len(item_list) > 0: 
            for item in item_list: 
                if item.condition > initial_condition: 
                    initial_condition = item.condition
                    best_item = item
        
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        
        if my_best_item != None and their_best_item != None:
            return self.swap_items(other, my_best_item, their_best_item)
        else: 
            return False 
            
            




            

