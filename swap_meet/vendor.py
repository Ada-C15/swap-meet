#_______________WAVE 1_______________________
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = []): 
        self.inventory = inventory 
        
        #self.inventory = list(inventory)
     
        
    def add(self, item):
        
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        
        for thing in self.inventory:
            if item == thing:
                self.inventory.remove(thing)
                return item
            
        return False         
        
#_______________WAVE 2_________________________
    #every instance of the item class becomes an element in the inventory list
    #returns list of class Item's objects inventory = [Item_a, Item_b, Item_c]
    def get_by_category(self, category):
        
        new_list_with_items = []
        
        #iterate on the list for each category (state) and check if the item is in there 
        for thing in self.inventory:
            if thing.category == category:
                new_list_with_items.append(thing)
    
        return new_list_with_items

        

#_______________Wave 3_________________________
          
            
    def swap_items(self, Vendor, my_item, their_item):
        
        my_inventory = self.inventory
        their_inventory = Vendor.inventory
        
        if self.does_item_exist(my_item, my_inventory) == False or self.does_item_exist(their_item, their_inventory) == False:
            return False

        # at this point, both vendors have item available to swap
        
        my_inventory.remove(my_item)
        their_inventory.append(my_item)
        
        their_inventory.remove(their_item)
        my_inventory.append(their_item)
        
        return True

    #helper function
    def does_item_exist(self, item, item_list):
        for i in item_list:
            if i == item:
                return True
            
        return False
         
 
            
#_______________wave 4___________________________

    def swap_first_items(self, Vendor):
        pass
        
        
        
#_______________wave 6___________________________
#composite class function
    def get_best_by_category(self, category = ""):
        pass
        #for thing in self.inventory
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        pass
        
        
        
        
        