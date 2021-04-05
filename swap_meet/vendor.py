# import pytest
# from swap_meet.Item import Item
# from swap_meet.vendor import Vendor


class Vendor:
    def __init__(self, inventory=None):
        if self.inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False
