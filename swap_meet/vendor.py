import swap_meet.item

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
        found_item_other = False
        found_item_self = False
        
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
        


    




