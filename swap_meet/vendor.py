from .item import Item
# ---- Wave 1 ----- #
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
        return items_list 

# ---- Wave 3 ----- #
    def swap_items(self, friend, my_item, their_item):
        swapped = False
        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.append(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            swapped= True
        return swapped

# ---- Wave 4 ----- #
    def swap_first_item(self, friend): 
        if not self.inventory or not friend.inventory: 
            return False 
        return self.swap_items(friend, self.inventory[0], friend.inventory[0])

# ---- Wave 6 ----- #
    def get_best_by_category(self, category): 
        category_items = self.get_by_category(category)
        items_conditions = []
        best_item = None
        for item in category_items: 
            items_conditions.append(item.condition)
            best_condition = max(items_conditions)
            if best_condition == item.condition:  
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority): 
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_best, their_best)