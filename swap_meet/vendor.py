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
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.inventory.remove(their_item)
            self.add(their_item)
            return True
        # else, return False
        else:
            return False