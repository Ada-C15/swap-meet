from swap_meet.item import Item

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
# you need to call the item.py file in order to access the category list 
# list of items in category list 
    def get_by_category(self,category):
        items = []
        for new_item in self.inventory:
            if new_item.category == category:
                items.append(new_item)
        return items




# ------------- Wave 4 -------------

    def swap_first_item(self,friend_vendor):
        if len(self.inventory) == 0 or len(friend_vendor.inventory) == 0:
                return False
        else:
            first_item = self.inventory[0]
            first_friend_item = friend_vendor.inventory[0]
            self.swap_items(friend_vendor,first_item,first_friend_item)
            return True 



# ------------- Wave 5 -------------
# this is using inheritance/ child and parent class and the super method


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
        # this will return the best item in my inventory that matches their_priority category
        my_category = self.get_best_by_category(their_priority)
        # this will return the best item from other inventory that matches from my_priority category
        other_category = other.get_best_by_category(my_priority)
        # invoking the method swap items that will swap the best items in their respective categories 
        
        total = self.swap_items(other,my_category,other_category) 

        return total

