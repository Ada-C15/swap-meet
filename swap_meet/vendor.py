# import pytest
# from swap_meet.item import Item


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

# ***WAVE2***
    def get_by_category(self, category):
        self.category = category
        items_matching_category = []
        for item in self.inventory:
            if item.category == category:
                items_matching_category.append(item)
        return items_matching_category
