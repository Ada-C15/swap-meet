#_______________WAVE 1_______________________

class Vendor:
    def __init__(self, inventory = []): #does not expect an argument to be passed
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

    def get_by_category(self, category):
        new_dict_of_items_category = {}
        
        for thing in self.inventory:
            new_dict_of_items_category[thing] = category
            
        return new_dict_of_items_category

#_______________Wave 3_________________________

    def swap_items(self, Vendor):
        self.item = my_item
        self.item = their_item
        
        #for things in Vendor:
            
            
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
        
        
        
        
        