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








# ------------- Wave 6  -------------