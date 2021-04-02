from swap_meet.item import Item

class Vendor: 
    def __init__(self, inventory=None):
        if inventory == None: 
            self.inventory = []
        else: 
            self.inventory = inventory 

    def add(self, item): 
            self.inventory.append(item)
            return item
        
    def remove(self, item): 
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False

# ---- Wave 2 ----- #

    def get_by_category(self, category): 
        items_list = []
        for item in self.inventory: 
            if category == item.category: 
                items_list.append(item)
                print(items_list)
        return items_list 
