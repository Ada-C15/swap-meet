from swap_meet.item import Item

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
        return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(self.remove(my_item))
            self.add(friend.remove(their_item))
            return True
        return False

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        self.swap_items(friend, self.inventory[0],friend.inventory[0])
        return True

    def get_best_by_category(self, wanted_category):
        items_in_category = self.get_by_category(wanted_category)
        if not items_in_category:
            return None
        best_condition = -1
        best_item = None
        for item in items_in_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        else: 
            self.swap_items(other, my_best_item, their_best_item)
            return True
