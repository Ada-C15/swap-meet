from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor():
    def __init__(self,inventory = None):
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
        return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True
        return False

    def swap_first_item(self, friend):
        if len(self.inventory) > 0 and len(friend.inventory) > 0:
            return self.swap_items(friend, self.inventory[0], friend.inventory[0])
        return False

    def get_best_by_category(self, category = ""):
        max_condition = -1
        best_item = None
        category_items = self.get_by_category(category)
        for item in category_items:
            if item.condition > max_condition:
                max_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_cat_item = self.get_best_by_category(their_priority)
        their_best_cat_item = other.get_best_by_category(my_priority)
        if my_best_cat_item != None and their_best_cat_item != None:
            return self.swap_items(other, my_best_cat_item, their_best_cat_item)
        return False



