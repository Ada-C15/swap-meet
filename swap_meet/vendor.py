from .item import Item

# WAVE 1

class Vendor:

    def __init__(self, inventory = None):
        if inventory is None:
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

    def get_by_category(self, category):
        
        matching_category_list = []

        for item in self.inventory:
            if item.category == category:
                matching_category_list.append(item)
        
        return matching_category_list

    def swap_items(self, vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        # if my_item in self.inventory:
        self.remove(my_item)
        vendor.add(my_item)

        
        # if their_item in vendor.inventory:
        vendor.remove(their_item)
        self.add(their_item)

        return True

    def swap_first_item(self, vendor):

        # consider first item in my inventory and first item in friend's inventory
        # remove first item from my inventory and add to friend's first item
        # remove first item from friend's inventory and add's my first item
        # return True
        # if either me or the friend have an empty inventory, return False

        # add/remove, assign

        if not self.inventory or not vendor.inventory:
            return False

        
        my_first_item = self.inventory[0]
        their_first_item = vendor.inventory[0]

        self.remove(my_first_item)
        vendor.add(my_first_item)
        
        vendor.remove(their_first_item)
        self.add(their_first_item)

        return True


    def get_best_by_category(self, category):

        if not self.get_by_category(category):
            return None

        condition_tracker = 0
        best_item = 0

        for item in self.get_by_category(category):
            if item.condition > condition_tracker:
                condition_tracker = item.condition
                best_item = item
        return best_item


    def swap_best_by_category(self, other, my_priority, their_priority):

        # comparing string to instances
        # if their_priority not in self.inventory or my_priority not in other.inventory:
        #     return False

        # their_priority and my_priority are each strings

        item_for_other = self.get_best_by_category(their_priority)
        item_for_self = other.get_best_by_category(my_priority)

        if not item_for_other or not item_for_self:
            return False

        # swap_items(self, vendor, my_item, their_item):

        return self.swap_items(other, item_for_other, item_for_self)

        
        




