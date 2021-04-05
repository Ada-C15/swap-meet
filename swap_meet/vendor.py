# import pytest
# from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=None):
        if self.inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item_to_remove in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

# ***WAVE2***
    def get_by_category(self, category):
        items_matching_category = []
        for items in self.inventory:
            if item.category == category:
                items_matching_category.append(items)
        return items_matching_category
