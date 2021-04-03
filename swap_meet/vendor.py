from swap_meet.item import Item
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
        self.friend = Vendor()
        self.my_item = my_item
        self.their_item = their_item
        for item in self.inventory: 
            if my_item in self.inventory and their_item in friend.inventory:
                self.inventory.remove(my_item)
                friend.inventory.append(my_item)
                self.inventory.append(their_item)
                friend.inventory.remove(their_item)
                return True
        else: 
            return False
        