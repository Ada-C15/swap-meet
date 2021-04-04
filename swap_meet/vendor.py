from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory or []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]
        # items = list(filter(lambda x: x.category == category, self.inventory))
        
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category) 
        if len(category_list) == 0:
            return None 
        best = max(category_list, key = lambda x: x.condition)
        return best

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)
        if not their_item or not my_item:
            return False
        return self.swap_items(other, my_item, their_item)
