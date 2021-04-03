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

#ODNE: turn into list comprehension
    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        # items = list(filter(lambda x: x.category == category, self.inventory))
        return items
        
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        item_being_swapped = self.remove(my_item)
        other_vendor.add(item_being_swapped)
        item_being_swapped = other_vendor.remove(their_item)
        self.add(item_being_swapped)
        return True

#DONEcall swap_item on first items
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

#DONE: call get by category
    def get_best_by_category(self, category):
        category_list = self.get_by_category(category) 
        if len(category_list) == 0:
            return None 
        best = max(category_list, key = lambda x: x.condition)
        return best

#Done:
    def swap_best_by_category(self, other, my_priority, their_priority):
        for_me = other.get_best_by_category(my_priority)
        for_them = self.get_best_by_category(their_priority)
        if not for_me or not for_them:
            return False
        return self.swap_items(other, for_them, for_me)
