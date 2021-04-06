from swap_meet.item import Item
# or is it from .item import Item
# what is the difference between these two type of imports

# ---------- Wave 1 -----------

class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory    
    
    def add(self, item):
        self.inventory.append(item)
        return item 
    

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    
    
    
# --------------- Wave 3 --------------   
    def swap_items(self,friend_vendor,my_item,their_item):  
        if my_item not in self.inventory or their_item not in friend_vendor.inventory: 
            return False
        else: 
            self.inventory.remove(my_item) 
            friend_vendor.inventory.append(my_item)
            friend_vendor.inventory.remove(their_item) 
            self.inventory.append(their_item)
            return True    






# --------------- Wave 2 --------------
# you need to call the item file in order to access the 
# category list 
# list of items in category list 
    def get_by_category(self,category):
        items = []
        for new_item in self.inventory:
            if new_item.category == category:
                items.append(new_item)
        return items




# ------------- Wave 4 -------------

    def swap_first_item(self,friend_vendor):
        # if not self.inventory or not friend_vendor.inventory:
        #     return False
        if len(self.inventory) == 0 or len(friend_vendor.inventory) == 0:
                return False
        else:
            first_item = self.inventory[0]
            first_friend_item = friend_vendor.inventory[0]
            # self.inventory.remove(first_item)
            self.swap_items(friend_vendor,first_item,first_friend_item)
            return True 



# ------------- Wave 5 -------------
# this is using inheritance and the super method


# ------------- Wave 6  -------------

    def get_best_by_category(self, category):
        highest_condition = 0
        quality_item = None
        matching_category_items = self.get_by_category(category)
        
        if matching_category_items == []:
            return None
        
        for item in matching_category_items:
            if item.condition > highest_condition:
                highest_condition = item.condition
                quality_item = item
        
        return quality_item        
        
    
    def swap_best_by_category(self,other,my_priority,their_priority):
        # this will return the best item from my priority category
        my_category = self.get_best_by_category(my_priority)
        # this will return the best item from thier priority category
        other_category = self.get_best_by_category(their_priority)

        # self.swap_items(friend_vendor,my_item,their_item):
        if other_category not in self.inventory or my_category not in other.inventory: 
            return False
        else: 
            self.inventory.remove(my_category) 
            other.inventory.append(my_category)
            other.inventory.remove(other_category) 
            self.inventory.append(other_category)
            return True      


