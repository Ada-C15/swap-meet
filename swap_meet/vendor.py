
class Vendor:

    def __init__(self, inventory = None):
        self.inventory = []
        if inventory: 
            self.inventory.extend(inventory) # self.inventory = inventory?

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
            vendor.inventory.append(my_item) # will call function later
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



