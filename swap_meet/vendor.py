
class Vendor:

    def __init__(self, inventory = None):
        self.inventory = []
        if inventory: 
            self.inventory.extend(inventory) 

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
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item) 
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            first_item = self.inventory[0]
            friend_item = vendor.inventory[0]
            return self.swap_items(vendor, first_item, friend_item)
        else:
            return False

    def get_best_by_category(self, category):
        best_condition = 0.0
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_best, their_best)

########################### This is the optional part #####################################

    def get_newest(self, age):
        least_old_item = 99
        newest_item = None
        for item in self.inventory:
            if item.age < least_old_item:
                least_old_item = item.age
                newest_item = item
        print(newest_item)
        return newest_item

    def swap_by_newest(self, other, my_newest, their_newest):
        pass