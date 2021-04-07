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
        if item not in self.inventory:
            return False
        else: 
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            vendor.inventory.remove(their_item)
            return True

        return False

    def swap_first_item(self, vendor):
        if len(self.inventory) >= 1 and len(vendor.inventory) >= 1:
            my_first_item = self.inventory[0]
            friend_first_item = vendor.inventory[0]
            return self.swap_items(vendor, my_first_item, friend_first_item)
            
        return False

    def get_best_by_category(self, category):
        max = 0
        the_best = None    
        for item in self.inventory:
            if item.category == category and item.condition > max:
                max = item.condition
                the_best = item
        return the_best
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_new_best = self.get_best_by_category(their_priority)
        their_new_best = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_new_best, their_new_best)
        
    def swap_by_newest(self, other, my_age, their_age):
        pass