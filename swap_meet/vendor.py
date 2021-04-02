from swap_meet.item import Item 

class Vendor:

    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory 

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category
    
    def swap_items(self, other_vendor, my_item, their_item):
        # if my_item in self.inventory AND their_item in other_vendor.inventory
            # remove my_item from self.inventory
            # and add my_item to other_ventory.inventory
            # remove their_item from other_vendor.inventory
            # and add their_item to self_inventory.inventory
            # return True
        # ???? tests pass with **.inventory.remove but not with **.inventory.add
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        else:
            other_vendor.add(self.inventory[0])
            self.remove(self.inventory[0])
            self.add(other_vendor.inventory[0])
            other_vendor.remove(other_vendor.inventory[0])
            return True

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if len(items_in_category) == 0:
            return None
        else:
            best_condition = 0
            for item in items_in_category:
                # ??? should below be > OR >= ???? 
                # thinking it needs to be >= because if we need to return an item even if all have a condition value of 0
                if item.condition >= best_condition:
                    best_condition = item.condition
                    best_item = item
            return best_item
