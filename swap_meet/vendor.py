#_______________WAVE 1_______________________
''' from item import Item
from clothing import Clothing
from decor import Decor
from electronics import Electronics '''

class Vendor:
    def __init__(self, inventory = None): 
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
     
        
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

#_______________Wave 3___________________________
   
    #helper function
    def does_item_exist(self, item, item_list):
        for i in item_list:
            if i == item:
                return True
            
        return False
            
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
            
#_______________wave 4___________________________

    def swap_first_item(self, Vendor):
        my_inventory = self.inventory
        their_inventory = Vendor.inventory
        
        #return flase if either of the 2 vendors have an empty list
        if (len(my_inventory) == 0) or (len(their_inventory) == 0):
           return False
        
        #remove first item from both vendors and add it to the other's list
        my_inventory.append(their_inventory.pop(0)) 
        their_inventory.append(my_inventory.pop(0))     
        
        return True
        
#_______________wave 6___________________________

    def get_best_by_category(self, category):
        
        best_item = None
        
        # step 1: Get list of items with the desired category
        new_list_by_category = self.get_by_category(category)
               
        # If there are no items in the inventory that match the category, it returns None       
        if len(new_list_by_category) == 0:
            return None       
        
        # step 2: Get the best item (with highest condition) from the list in Step1, if there are matching items category
        list_by_condition = []
        
        for thing in new_list_by_category:
            list_by_condition.append(thing.condition)
            
        max_condition_value = max(list_by_condition) 
        
        #returns a single item even if there are duplicates with best condtition filtered by category
        for thing in new_list_by_category:
            if thing.condition == max_condition_value:
                best_item = thing
                break
            
        return best_item
    
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        
        #call the function with the correct parameter to get the best_item for self and other
        my_best_item = self.get_best_by_category(their_priority)
        
        their_best_item = other.get_best_by_category(my_priority)
        
        #Fail first if either of the inventory is empty
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        
        #fail second if best item is None for either vendor
        if my_best_item == None or their_best_item == None:
            return False
        
        #fail third if the best item category for either vendor doesn't match 
        if my_best_item.category != their_priority or their_best_item.category != my_priority:
           return False
        
        #calling swap item function from wave 3
        return self.swap_items(other, my_best_item, their_best_item)
        
    
        #OMMITED LINES OF CODE DUE TO DRY YOUR CODE
        ''' #if the categories match then remove the best item from self vendor to other vendor
        self_sawp_item = self.swap_item(self.inventory, other.inventory, my_best_item)
        
        other_swap_item = self.swap_item(other.inventory, self.inventory, their_best_item) 
        
        

    #helper function   
    def swap_item(self, inventory_list_1, inventory_list_2, best_item):
        for i in inventory_list_1:
            if i == best_item:
                inventory_list_1.remove(best_item)
                inventory_list_2.append(best_item)
                break 

        #used helper to condense these lines of code further
        for thing in self.inventory:
            if thing == my_best_item:
                self.inventory.remove(my_best_item)
                other.inventory.append(my_best_item)
                break
        
        #remove the best_item of other vendor and add to self vendor  
        for thing in other.inventory:
            if thing == their_best_item:
                other.inventory.remove(their_best_item)
                self.inventory.append(their_best_item)
                break '''
            
    
    
        
#____________optional enhancement__________________  

    def swap_by_newest(self):
        pass   
        
        