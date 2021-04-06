
# import pytest
from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return item

    def remove(self, item):
        self.item = item
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

# ***WAVE 2***

    def get_by_category(self, category):
        items_matching_category = []
        for item in self.inventory:
            if category == item.category:
                items_matching_category.append(item)
        return items_matching_category

# ***WAVE 3***

    def swap_items(self, Vendor, my_item, their_item):
        if (my_item in self.inventory) and (their_item in Vendor.inventory):
            self.remove(my_item)
            self.add(their_item)
            Vendor.add(my_item)
            Vendor.remove(their_item)
            return True
        else:
            return False

# ***WAVE 4***
    def swap_first_item(self, Vendor):
        # self.Vendor = Vendor
        if (self.inventory and Vendor.inventory):
            return self.swap_items(Vendor, self.inventory[0], Vendor.inventory[0])
        return False
