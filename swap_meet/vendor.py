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


# ------------- Wave 3 -------------
#          