from swap_meet.item import Item

class Vendor():

    def __init__(self, inventory = None):

        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        

    def add(self, item):  
        self.inventory.append(item)
        return item
        

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            for i, element in enumerate(self.inventory):
                if element == item:
                    return self.inventory.pop(i)          
        
    
    def get_by_category(self, category):
        category_list = []
        i = 0
        while len(self.inventory) > i:
            for vendor_item in self.inventory:
                if category == vendor_item.category:
                    category_list.append(vendor_item)
                i+=1               
            return category_list
    
    def swap_items(self, other_vendor, self_item, other_item):
        
        if self_item not in self.inventory or other_item not in other_vendor.inventory:
            return False

        for item in other_vendor.inventory:
            if item == other_item:
                other_vendor.inventory.remove(item)
                other_vendor.inventory.append(self_item)       
            
        for item in self.inventory:
            if item == self_item:
                self.inventory.remove(item)
                self.inventory.append(other_item)
        
        return True
    
    def swap_first_item(self, other_vendor):

        if len(other_vendor.inventory) == 0 or len(self.inventory) == 0: 
            return False
        
        first_item_self = self.inventory[0]
        first_item_other = other_vendor.inventory[0]

        for item in other_vendor.inventory:
            other_vendor.inventory[0] = first_item_self

        for item in self.inventory:
            self.inventory[0] = first_item_other
            
        return True
    
    def get_best_by_category(self, category):

        best_list = []
        compare_dic = {}
        max_val = ""
        mismatched = []
    
        #if category not in self.inventory:
            #return None
        
        for item in self.inventory:         
            if item.category == category:
                best_list.append(item)
            elif item.category != category:
                mismatched.append(item)
        
        if len(mismatched) == len(self.inventory):
            return None
        
        else:
            max_val = max(best_list, key=lambda item: item.condition)
            return max_val


        
    def test_swap_best_by_category(self, other, my_priority, their_priority):

        their_priority_best = ""
        my_priority_best = ""

        for item in self.inventory:
            if their_priority == item.category:
                their_priority_best = self.get_best_by_category(their_priority)
        
        
        for item in other.inventory:
            if my_priority == item.category:
                my_priority_best = other.get_best_by_category(my_priority)
        
        for item in other.inventory:
            if item == my_priority_best:
                other.remove(item)
                other.inventory.append(their_priority_best)       
            
        for item in self.inventory:
            if item == their_priority_best:
                self.inventory.remove(item)
                self.inventory.append(my_priority_best)
        
    #self.swap_items(other, my_priority_best, their_priority_best)
        
        


        

        
        


    




